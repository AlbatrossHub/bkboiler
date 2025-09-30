# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class MrpProduction(models.Model):
    """ Manufacturing Orders """
    _inherit = 'mrp.production'

    customer_id = fields.Many2one("res.partner", string="Client Name")
    sos_no = fields.Char(string="SOS #")