from odoo import fields, models, _
from datetime import timedelta


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

    def open_wizard_message(self):
        for rec in self:
            context = dict(self.env.context)
            view = self.env.ref("ampalibe.send_message_wizard")
            active_ids = self.env.context.get("active_ids", [])
            user_ids = self.env["amp.user"].search(
                [
                    (
                        "last_use",
                        ">",
                        fields.datetime.now() - timedelta(hours=24),
                    ),
                    ("id", "in", active_ids),
                ]
            )
            user_ids = user_ids.ids
            if rec.id:
                if rec.last_use > fields.datetime.now() - timedelta(hours=24):
                    user_ids.append(rec.id) if rec.id not in user_ids else None
            context.update({"default_amp_user_ids": user_ids})
            res = self.env["amp.message"].create(
                {
                    "amp_user_ids": [(6, 0, user_ids)],
                }
            )
            return {
                "name": _("Send message by Ampalibe"),
                "type": "ir.actions.act_window",
                "view_type": "form",
                "view_mode": "form",
                "res_model": "amp.message",
                "views": [(view.id, "form")],
                "view_id": view.id,
                "target": "new",
                "res_id": res.id,
                "context": context,
            }
