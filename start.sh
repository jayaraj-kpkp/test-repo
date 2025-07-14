#!/bin/bash
exec python3 odoo-bin -c odoo.conf -d saudi_sales_db -i sale,account,sale_management,l10n_sa --stop-after-init



