{
    'name': 'invoice_erp',
    'version': '1.0',
    'summary': 'Customized invoice layout with bilingual support and bank details',
    'description': 'Overrides the standard invoice PDF report in Odoo 18 to match company format.',
    'author': 'Your Name or Company',
    'category': 'Accounting',
    'depends': ['account'],
    'data': [
        'views/invoice_report.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

# {
#     "name": "Custom Invoice Layout",
#     "version": "1.0",
#     "summary": "Customized invoice template with bilingual header, QR code, and bank details",
#     "description": """
#         This module customizes the standard invoice PDF layout to match the company's requirements,
#         including Arabic-English headers, QR code generation, and custom styling.
#     """,
#     "category": "Accounting",
#     "author": "Your Company Name",
#     "website": "https://yourcompanywebsite.com",
#     "license": "LGPL-3",
#     "depends": [
#         "account",
#     ],
#     "data": [
#         "views/report_invoice.xml",
#     ],
#     "assets": {},
#     "installable": True,
#     "application": False,
#     "auto_install": False,
# }
