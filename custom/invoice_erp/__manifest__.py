{
    "name": "Saudi Invoice Format",
    "version": "1.0",
    "depends": ["account"],
    "author": "Your Company",
    "category": "Accounting",
    "summary": "Saudi Arabia style tax invoice format",
    "description": """
Saudi Arabia Tax Invoice with Arabic and English fields, VAT breakdown, and custom layout.
    """,
    "data": [
        "views/report_action_override.xml",
        "report/report.xml",
        "report/report_invoice.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}

