# Copyright <2024> <Ivan>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Helpdesk Ivan Vidal",
    "version": "14.0.1.0.0",
    "author": "AEODOO, Odoo Community Association (OCA)",
    "license": "AGPL-3",

    "depends": [
        "base",
    ],

    "data": [
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "views/helpdesk_menu.xml",
        "views/helpdesk_view.xml",
    ],

    'images': [
        'static/description/icon.png',  # Ruta relativa al logo de tu módulo
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}