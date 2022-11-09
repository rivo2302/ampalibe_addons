# -*- coding: utf-8 -*-
{
    "name": "Ampalibe sale",
    "summary": """
        An odoo module to manage a Messenger bot from the Ampalibe Framework with sale module odoo.
    """,
    "author": "Rivo2302",
    "website": "https://github.com/rivo2302/ampalibe_odoo",
    "live_test_url": "https://www.youtube.com/watch?v=DOF95xoPXq0",
    "license": "LGPL-3",
    "support": "rivo2302@gmail.com",
    "category": "Chatbot",
    "images": ["static/img/background.png"],
    "version": "15.0.1.1.1",
    "price": "0",
    "currency": "USD",
    "development_status": "Production/Stable",
    "maintainers": ["rivo2302"],
    "depends": ["base", "ampalibe", "sale"],
    "data": [
        "views/amp_user.xml",
    ],
    "installable": True,
    "application": False,
}
