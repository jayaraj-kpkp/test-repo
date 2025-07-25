{
    'name': 'Custom Quotation Report SA',
    'version': '1.0',
    'summary': 'Customized Quotation Format for Saudi Arabia',
    'description': 'Adds a custom Quotation (Sale Order) print format with Arabic labels.',
    'author': 'YourName',
    'category': 'Sales',
    'depends': ['sale'],
    'data': [
        'views/report_saleorder_document_inherit.xml',

    ],
    'installable': True,
    'application': True,  # ✅ Add this to show in Apps
    'auto_install': False,
}
