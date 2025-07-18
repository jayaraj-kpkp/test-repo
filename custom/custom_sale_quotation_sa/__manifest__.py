{
    'name': 'Custom Quotation Report SA',
    'version': '1.0',
    'summary': 'Customized Quotation Format for Saudi Arabia',
    'description': 'Adds a custom Quotation (Sale Order) print format with Arabic labels.',
    'author': 'YourName',
    'category': 'Sales',
    'depends': ['sale'],
    'data': [
        'views/sale_report_templates.xml',
    ],
    'installable': True,
    'application': True,  # ✅ Add this to show in Apps
    'auto_install': False,
}
