from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    delivery_terms = fields.Char(string="Delivery Terms")
    po_number_ar = fields.Char(string="P.O Number Arabic")
