from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    sov_ids = fields.One2many("commission.sale.sov", "sale_id", string="SOV Lines")
