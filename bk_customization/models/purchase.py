# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    use_purchase_order_note = fields.Boolean(
        string='Default(s) Terms & Conditions')
    purchase_order_note = fields.Html(
        string='Default Term(s) and Condition(s)', translate=True)


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    use_purchase_order_note = fields.Boolean(
        related='company_id.use_purchase_order_note', readonly=False,
        string='Default(s) Terms & Conditions')
    purchase_order_note = fields.Html(
        related='company_id.purchase_order_note', readonly=False,
        string="Conditions & Terms")


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.model
    def _default_note(self):
        if self.env.user.company_id.use_purchase_order_note:
            return self.env.user.company_id.purchase_order_note
        return ''

    note = fields.Html('Terms and Conditions', default=_default_note)
    customer_id = fields.Many2one("res.partner", string="Client Name")