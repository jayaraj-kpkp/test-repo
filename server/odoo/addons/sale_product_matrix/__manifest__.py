# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "Sale Matrix",
    'summary': "Add variants to Sales Order through a grid entry.",
    'description': """
This module allows to fill Sales Order rapidly
by choosing product variants quantity through a Grid Entry.
    """,
    'category': 'Sales/Sales',
    'version': '1.0',
    'depends': ['sale', 'product_matrix'],
    'data': [
        'views/product_template_views.xml',
        'views/sale_order_views.xml',
        'report/report_saleorder_document_inherit.xml',
    ],
    'demo': [
        'data/product_matrix_demo.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'sale_product_matrix/static/src/**/*',
        ],
    },
    'license': 'LGPL-3',
}
