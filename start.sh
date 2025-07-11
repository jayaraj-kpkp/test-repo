#!/bin/bash
exec python3 odoo-bin -c odoo.conf -i sale_management,stock,purchase,account --stop-after-init
