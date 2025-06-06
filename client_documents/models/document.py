from odoo import api, fields, models, _

class Document(models.Model):
    _inherit = 'documents.document'

    is_verify = fields.Boolean(string='Is Verify')
    number = fields.Char(
        string='Number', required=True, copy=False, readonly=True,
        index=True, default=lambda self: _('New'), tracking=True)

    def action_numbers(self):
        docs = self.env['documents.document'].sudo().search([])
        for doc in docs:
            doc.number = self.env['ir.sequence'].next_by_code('documents.document') or _('New')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'number' not in vals:
                vals['number'] = self.env['ir.sequence'].next_by_code('documents.document') or _('New')
        return super(Document, self).create(vals_list)
