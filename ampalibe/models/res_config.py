from odoo import fields, api, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    amp_url = fields.Char("Url", help="URL of Ampalibe server")
    page_id = fields.Char("ID", help="Facebook Page ID")
    token = fields.Char("Token", help="Facebook Token")

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(
            amp_url=self.env["ir.config_parameter"]
            .sudo()
            .get_param("ampalibe.amp_url"),
            page_id=self.env["ir.config_parameter"]
            .sudo()
            .get_param("ampalibe.page_id"),
            token=self.env["ir.config_parameter"].sudo().get_param("ampalibe.token"),
        )
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        param = self.env["ir.config_parameter"].sudo()
        param.set_param("ampalibe.amp_url", self.amp_url)
        param.set_param("ampalibe.page_id", self.page_id)
        param.set_param("ampalibe.token", self.token)
