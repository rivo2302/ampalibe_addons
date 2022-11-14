from odoo import api, fields, models, _


class AmpPersonas(models.Model):
    """
    Personas management models of Ampalibe framework.
    """

    _name = "amp.personas"
    _description = "Ampalibe Personas"

    name = fields.Char("Name")
    fid = fields.Char("Facebook ID")
    description = fields.Text("Description")
    image = fields.Binary("Image")
    image_url = fields.Char(
        "Image url", compute="_compute_image_url", store=True
    )

    @api.depends("image")
    def _compute_image_url(self):
        for rec in self:
            rec.image_url = "/web/image/amp.personas/%s/image" % rec.id

    default = fields.Boolean("Default")

    def sync_personas(self):
        """
        Sync personas from Ampalibe server.
        """

        message = _("Starting progress : Synchronise personas 002")
        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "message": message,
                "type": "info",
                "sticky": False,
                "next": {"type": "ir.actions.act_window_close"},
            },
        }

    def synchronise(self):
        print("teste")
