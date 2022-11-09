from odoo import api, fields, models, _


class AmpUser(models.Model):
    _name = "amp.user"
    _rec_name = "name"
    _order = "last_use desc"
    _description = "User management models of Ampalibe framework."

    name = fields.Char("Name")
    user_id = fields.Char("Facebook ID")
    lang = fields.Selection(
        [("fr", "FR"), ("mg", "MG"), ("en", "EN")],
        "Language",
        default="fr",
        required=True,
    )
    action = fields.Char("Action")
    tmp = fields.Char("Temporary variables")

    last_use = fields.Datetime(
        "Last modified", default=lambda self: fields.datetime.now()
    )
    _sql_constraints = [
        (
            "unique_user_id",
            "unique(user_id)",
            "The Facebook id of each user must be unique.",
        )
    ]
