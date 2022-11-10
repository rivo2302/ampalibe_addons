from odoo import fields, api, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    amp_url = fields.Char(
        "Url",
        help="URL of Ampalibe server",
        config_parameter="ampalibe.amp_url",
    )
    page_id = fields.Char(
        "ID",
        help="Facebook Page ID",
        config_parameter="ampalibe.page_id",
    )
    token = fields.Char(
        "Token",
        help="Facebook Token",
        config_parameter="ampalibe.token",
    )
    main_personas = fields.Many2one(
        "amp.personas",
        "Main Personas",
        config_parameter="ampalibe.main_personas",
    )

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
            token=self.env["ir.config_parameter"]
            .sudo()
            .get_param("ampalibe.token"),
        )
        return res

    @api.model
    def set_values(self):
        param = self.env["ir.config_parameter"].sudo()
        param.set_param("ampalibe.amp_url", self.amp_url)
        param.set_param("ampalibe.page_id", self.page_id)
        param.set_param("ampalibe.token", self.token)
        super(ResConfigSettings, self).set_values()

    @api.onchange("main_personas")
    def _onchange_main_personas(self):
        self.env["amp.personas"].search([]).write({"default": False})
        if self.main_personas:
            self.main_personas.write({"default": True})

    def action_sync_personas(self):
        return self.env["amp.personas"].sync_personas()
