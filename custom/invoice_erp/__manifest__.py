{
    "name": "Saudi Invoice Format",
    "version": "1.0",
    "depends": ["account", "sale"],
    "author": "Your Company",
    "category": "Accounting",
    "summary": "Saudi Arabia style tax invoice format",
    "description": """
Saudi Arabia Tax Invoice with Arabic and English fields, VAT breakdown, and custom layout.
    """,
    "data": [
        "views/sale_order_view.xml",
        "views/report_action_override.xml",
        "report/report_invoice.xml",
        "views/dashboard_view.xml",
        "views/account_move_view.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}

