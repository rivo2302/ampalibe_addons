from odoo import api, fields, models, _


class AmpUserModel(models.Model):
    _name = "amp.user"
    _rec_name = "user_id"
    _order = "last_use desc"
    _description = "User management models of Ampalibe framework."

    user_id = fields.Char("Facebook ID")
    lang = fields.Selection(
        [("fr", "FR"), ("mg", "MG"), ("en", "EN")],
        "Language",
        default="fr",
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
