from odoo import models, fields, api
import base64
import qrcode
from io import BytesIO
from datetime import datetime


class AccountMove(models.Model):
    _inherit = 'account.move'

    qr_code_image = fields.Binary("QR Code (ZATCA)", compute="_compute_qr_code", store=True)

    @api.depends('invoice_date', 'amount_total', 'amount_tax', 'company_id.vat')
    def _compute_qr_code(self):
        for rec in self:
            if rec.company_id.vat:
                rec.qr_code_image = rec._generate_qr_code()
            else:
                rec.qr_code_image = False

    def _generate_qr_code(self):
        self.ensure_one()

        def _encode_tag(tag, value):
            value_bytes = value.encode('utf-8')
            return bytes([tag]) + bytes([len(value_bytes)]) + value_bytes

        # Required data
        seller_name = self.company_id.name or ""
        seller_vat = self.company_id.vat or ""
        invoice_date = (
            self.invoice_date.strftime('%Y-%m-%dT%H:%M:%S')
            if self.invoice_date else ""
        )
        invoice_total = "{0:.2f}".format(self.amount_total)
        vat_total = "{0:.2f}".format(self.amount_tax)

        # ZATCA encoding
        qr_bytes = (
            _encode_tag(1, seller_name) +
            _encode_tag(2, seller_vat) +
            _encode_tag(3, invoice_date) +
            _encode_tag(4, invoice_total) +
            _encode_tag(5, vat_total)
        )

        # Generate QR code image
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=4,
            border=1,
        )
        qr.add_data(qr_bytes)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        qr_image_base64 = base64.b64encode(buffer.getvalue())  # return raw bytes, no `.decode()`

        return qr_image_base64
