#!/usr/bin/env bash
#exec python odoo-bin -c odoo.conf
#!/bin/bash
exec python3 odoo-bin -c odoo.conf -d postgresql_odoo18_1 -i base --log-level=debug



