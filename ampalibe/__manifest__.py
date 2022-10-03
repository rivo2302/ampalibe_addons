# -*- coding: utf-8 -*-
{
    "name": "ampalibe",
    "summary": """
        An odoo module to manage a Messenger bot from the Ampalibe Framework.
    """,
    "description": """
        - Ampalibe is a lightweight Python framework for building Facebook Messenger bots faster. 
    It provides a new concept, it manages webhooks, processes data sent by Facebook and provides 
    API Messenger with advanced functions such as payload management, item length, and more.
        - Odoo. ERP Open Source Apps. To Grow Your Business.
        
        This addons is to link Ampalibe framework with Odoo. Then you can use Odoo as a database for your bot, and
    have your backoffice of your chabtot directly in Odoo Interface.
    """,
    "author": "rivo2302(iteam-$)",
    "website": "https://github.com/rivo2302/ampalibe_odoo",
    "license": "LGPL-3",
    "installable": True,
    "category": "Chatbot",
    "version": "15.0.1.1.1",
    "development_status": "Production/Stable",
    "maintainers": ["rivo2302"],
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/amp_user.xml",
    ],
}
