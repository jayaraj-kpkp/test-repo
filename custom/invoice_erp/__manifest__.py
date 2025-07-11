{
    'name': "invoice_erp",
    'version': '1.0',
    'summary': "Custom Invoice Template",
    'description': "This module customizes the invoice layout.",
    'author': "Your Name",
    'website': "https://yourcompany.com",
    'category': 'Accounting',
    'depends': ['account'],
    'data': [
        'views/report_invoice.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            'invoice_erp/static/src/css/invoice_styles.css',
        ],
    },
    'installable': True,
    'application': False
}
