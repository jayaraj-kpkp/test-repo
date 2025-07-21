# from odoo import models
#
# class AccountMove(models.Model):
#     _inherit = 'account.move'


from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    po_number = fields.Char(string='P.O Number')
    delivery_date = fields.Date(string='Delivery Date')
