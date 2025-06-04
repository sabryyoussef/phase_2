from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools.misc import clean_context

class DocumentRequest(models.TransientModel):
    """
    Document Request Wizard
    Enhanced document request wizard with project integration and improved partner management
    """
    _inherit = 'documents.request_wizard'
    _description = 'Document Request Wizard Extension'

    project_id = fields.Many2one(
        'project.project',
        string='Project',
        tracking=True,
        help='Related project for the document request'
    )
    
    partner_ids = fields.Many2many(
        'res.partner',
        relation='document_request_partner_rel',
        column1='request_wizard_id',
        column2='partner_id',
        string='Available Partners',
        compute='_compute_project_partners',
        help='Partners available for document request'
    )
    
    partner_id = fields.Many2one(
        'res.partner',
        string='Requested Partner',
        domain="[('id', 'in', partner_ids)]",
        tracking=True,
        help='Partner to request the document from'
    )
    
    type_id = fields.Many2one(
        'res.partner.document.type',
        string='Document Type',
        tracking=True,
        required=True,
        help='Type of document being requested'
    )
    
    deadline = fields.Date(
        string='Request Deadline',
        tracking=True,
        default=lambda self: fields.Date.today() + relativedelta(days=7),
        help='Deadline for document submission'
    )
    
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High'),
        ('3', 'Urgent')
    ], string='Priority',
        default='1',
        tracking=True,
        help='Priority level of the document request'
    )
    
    notes = fields.Text(
        string='Additional Notes',
        tracking=True,
        help='Additional information about the document request'
    )
    
    request_status = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Request Sent'),
        ('received', 'Document Received'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled')
    ], string='Request Status',
        default='draft',
        tracking=True,
        help='Current status of the document request'
    )
    
    document_count = fields.Integer(
        string='Document Count',
        compute='_compute_document_count',
        help='Number of documents received for this request'
    )
    
    last_reminder_date = fields.Datetime(
        string='Last Reminder',
        tracking=True,
        help='Date of the last reminder sent'
    )
    
    reminder_count = fields.Integer(
        string='Reminder Count',
        default=0,
        tracking=True,
        help='Number of reminders sent'
    )

    @api.depends('project_id')
    def _compute_project_partners(self):
        for rec in self:
            if rec.project_id:
                # Get all relevant partners from the project
                partners = rec.project_id.compliance_shareholder_ids.mapped('contact_id')
                partner_list = [
                    rec.project_id.partner_id.id,
                    rec.project_id.hand_partner_id.id
                ] + partners.ids
                rec.partner_ids = [(6, 0, partner_list)]
            else:
                # If no project, show all partners
                rec.partner_ids = [(6, 0, self.env['res.partner'].search([]).ids)]

    @api.depends('partner_id', 'type_id')
    def _compute_document_count(self):
        for rec in self:
            if rec.partner_id and rec.type_id:
                rec.document_count = self.env['documents.document'].search_count([
                    ('partner_id', '=', rec.partner_id.id),
                    ('type_id', '=', rec.type_id.id),
                    ('project_id', '=', rec.project_id.id if rec.project_id else False)
                ])
            else:
                rec.document_count = 0

    @api.constrains('deadline', 'priority')
    def _check_deadline_priority(self):
        for rec in self:
            if rec.deadline and rec.priority == '3':  # Urgent priority
                if rec.deadline > fields.Date.today() + relativedelta(days=3):
                    raise ValidationError(_('Urgent requests should have a deadline within 3 days.'))

    def action_send_reminder(self):
        self.ensure_one()
        if self.request_status == 'sent':
            # Implement reminder logic here
            self.write({
                'last_reminder_date': fields.Datetime.now(),
                'reminder_count': self.reminder_count + 1
            })
            # Send reminder email
            template = self.env.ref('documents.mail_template_document_request_reminder', False)
            if template:
                template.with_context(
                    lang=self.partner_id.lang,
                    email_layout_xmlid='mail.mail_notification_light'
                ).send_mail(self.id, force_send=True)
        return True

    def request_document(self):
        """Override the original request_document method with enhanced functionality"""
        self.ensure_one()
        
        # Validate request
        if not self.partner_id:
            raise UserError(_('Please select a partner for the document request.'))
        if not self.type_id:
            raise UserError(_('Please select a document type.'))
        
        # Create the document request
        document = super(DocumentRequest, self).request_document()
        
        # Update document with additional information
        if document and self.project_id:
            document.write({
                'project_id': self.project_id.id,
                'type_id': self.type_id.id,
                'deadline': self.deadline,
                'priority': self.priority,
                'notes': self.notes,
                'request_status': 'sent'
            })
            
            # Send notification
            self._send_document_request_notification(document)
        
        return document

    def _send_document_request_notification(self, document):
        """Send notification about the document request"""
        self.ensure_one()
        template = self.env.ref('documents.mail_template_document_request', False)
        if template:
            template.with_context(
                lang=self.partner_id.lang,
                email_layout_xmlid='mail.mail_notification_light'
            ).send_mail(document.id, force_send=True)

    def action_cancel_request(self):
        """Cancel the document request"""
        self.ensure_one()
        if self.request_status in ['draft', 'sent']:
            self.write({
                'request_status': 'cancelled',
                'notes': f"{self.notes or ''}\nCancelled by {self.env.user.name} on {fields.Datetime.now()}"
            })
        return True

    def action_mark_received(self):
        """Mark the document as received"""
        self.ensure_one()
        if self.request_status == 'sent':
            self.write({
                'request_status': 'received',
                'notes': f"{self.notes or ''}\nDocument received on {fields.Datetime.now()}"
            })
        return True

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('project_id'):
                project = self.env['project.project'].browse(vals['project_id'])
                if not vals.get('partner_id') and project.partner_id:
                    vals['partner_id'] = project.partner_id.id
        return super(DocumentRequest, self).create(vals_list)

    def write(self, vals):
        if 'request_status' in vals and vals['request_status'] == 'sent':
            vals['last_reminder_date'] = fields.Datetime.now()
        return super(DocumentRequest, self).write(vals) 