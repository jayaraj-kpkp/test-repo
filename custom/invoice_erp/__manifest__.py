{
    'name': 'Custom Invoice Template',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Overrides and customizes invoice template',
    'author': 'Your Company',
    'depends': ['account'],
    'data': [
        'views/report_invoice.xml',
    ],
    'installable': True,
    'application': False,
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
