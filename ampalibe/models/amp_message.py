from odoo import fields, api, models, _


class AmpMessage(models.Model):
    _name = "amp.message"
    _description = "Ampalibe Message to send in Messenger"

    name = fields.Char(
        string="Message Name",
    )
    message = fields.Text(string="Message")
    status = fields.Selection(
        [
            ("draft", "Draft"),
            ("loading", "Loading"),
            ("sent", "Sent"),
            ("error", "Error"),
        ],
        default="draft",
        string="Status",
    )
    amp_user_ids = fields.Many2many(
        "amp.user",
        string="Users",
        relation="amp_message_amp_user_rel",
        column1="amp_message_id",
        column2="user_id",
    )
    attachment_ids = fields.Many2many("ir.attachment", string="Attachements")

    def send_message(self):
        self.sudo().write({"status": "loading"})
        message = _(
            "Info : Your message has been sent to your Ampalibe servers. "
        )
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

    def close(self):
        return None
