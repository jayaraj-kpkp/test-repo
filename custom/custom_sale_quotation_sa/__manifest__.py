{
    'name': 'Custom Quotation Report SA',
    'version': '1.0',
    'summary': 'Customized Quotation Format for Saudi Arabia',
    'description': 'Adds a custom Quotation (Sale Order) print format with Arabic labels.',
    'author': 'YourName',
    'category': 'Sales',
    'depends': ['sale'],
    'data': [
        'views/report_action_custom_quotation.xml',
        'views/report_quotation_template.xml',
        'views/report_action_override.xml',
    ],
    'installable': True,
    'application': True,  # ✅ Add this to show in Apps
    'auto_install': False,
}
