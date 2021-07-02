# Copyright Sudokeys (www.sudokeys.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Purchase Subscription",
    "summary": "TODO",
    "version": "14.0.0.0.1",
    "development_status": "Production/Stable",
    "category": "Inventory/Purchase",
    "images": ["static/description/banner.png"],
    "website": "https://github.com/OCA/None",
    "author": "Sudokeys, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "application": True,
    "depends": ["base", "account", "analytic"],
    "data": [
        # Datas
        "data/purchase_subscription_data.xml",
        # Security
        "security/purchase_subscription_security.xml",
        "security/ir.model.access.csv",
        # Views
        "views/product_template_views.xml",
        "views/res_partner_views.xml",
        "views/purchase_subscription_views.xml",
        "views/account_move_views.xml",
    ],
}
