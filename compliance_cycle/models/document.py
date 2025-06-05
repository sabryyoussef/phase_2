from odoo import api, fields, models


class Documents(models.Model):
    _inherit = "documents.document"

    onboarding_id = fields.Many2one("initial.client.onboarding", string="Onboarding")


class ProductDocuments(models.Model):
    _inherit = "product.template.required.documents"

    rating_id = fields.Many2one("risk.rating", string="Rating")


class TaskRequiredLines(models.Model):
    _inherit = "task.document.required.lines"

    onboarding_id = fields.Many2one("initial.client.onboarding", string="Onboarding")
    document = fields.Binary(string="Document")

    def fitch_document(self):
        # Implement the logic for fetching documents
        for record in self:
            # Example logic: Fetch documents based on some criteria
            documents = self.env["documents.document"].search(
                [("onboarding_id", "=", record.onboarding_id.id)]
            )
            record.write({"document": documents.mapped("datas")})
