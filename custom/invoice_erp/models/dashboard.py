from odoo import models, fields, api

class InvoiceDashboard(models.Model):
    _name = 'invoice.dashboard'
    _description = 'Invoice Dashboard'

    name = fields.Char(string='Name', default='Invoice Dashboard')
    total_invoices = fields.Integer(string='Total Invoices', compute='_compute_totals')
    total_amount = fields.Float(string='Total Amount', compute='_compute_totals')

    @api.depends()
    def _compute_totals(self):
        invoice_model = self.env['account.move'].search([('move_type', '=', 'out_invoice')])
        for record in self:
            record.total_invoices = len(invoice_model)
            record.total_amount = sum(invoice_model.mapped('amount_total'))
