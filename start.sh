#!/bin/bash
exec python3 odoo-bin -c odoo.conf -d postgresql_name_odoo18_software -i base,sale --stop-after-init
