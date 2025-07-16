import base64
import qrcode
from io import BytesIO
from odoo import models
from odoo import models, fields
class AccountMove(models.Model):
    _inherit = 'account.move'
    qr_code_image = fields.Binary(
        string="ZATCA QR Code",
        compute="_compute_qr_code_image",
        store=False
    )

    def _compute_qr_code_image(self):
        for rec in self:
            rec.qr_code_image = rec._generate_qr_code()

    def _generate_qr_code(self):
        self.ensure_one()
        # ZATCA Tag Encoding:
        # Tag 1: Seller Name
        # Tag 2: VAT Number
        # Tag 3: Invoice Date (ISO8601)
        # Tag 4: Invoice Total
        # Tag 5: VAT Total

        def _encode_tag(tag, value):
            value_bytes = value.encode('utf-8')
            return bytes([tag]) + bytes([len(value_bytes)]) + value_bytes

        seller_name = self.company_id.name or ""
        seller_vat = self.company_id.vat or ""
        invoice_date = self.invoice_date.strftime('%Y-%m-%dT%H:%M:%S') if self.invoice_date else ""
        invoice_total = "{0:.2f}".format(self.amount_total)
        vat_total = "{0:.2f}".format(self.amount_tax)

        qr_bytes = (
            _encode_tag(1, seller_name) +
            _encode_tag(2, seller_vat) +
            _encode_tag(3, invoice_date) +
            _encode_tag(4, invoice_total) +
            _encode_tag(5, vat_total)
        )
        qr_base64 = base64.b64encode(qr_bytes).decode('utf-8')

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=4,
            border=1,
        )
        qr.add_data(qr_base64)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        return base64.b64encode(buffer.getvalue())
