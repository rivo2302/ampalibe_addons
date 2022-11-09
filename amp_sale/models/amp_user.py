from odoo import api, fields, models, _


class AmpUser(models.Model):
    _inherit = "amp.user"

    sale_order_count = fields.Integer(
        "Sale order count", compute="_compute_sale_order_ids"
    )

    @api.depends("tmp")
    def _compute_sale_order_ids(self):
        for rec in self:
            rec.sale_order_count = 1
