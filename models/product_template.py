# -*- coding: utf-8 -*-
from odoo.exceptions import   UserError, RedirectWarning
import odoo.addons.decimal_precision as dp
from odoo import models, fields, api


class ProductTemplateCost(models.Model):
    _inherit = 'product.template'
    product_cost = fields.Float('Costo', digits=dp.get_precision('Product Price'),groups="purchase.group_purchase_manager",help = "Costo referencial del producto. ")

    @api.model
    def _default_Ccurrency(self):
        return self.env.user.company_id.currency_id


    cost_currency_id = fields.Many2one('res.currency', string="Moneda para costo", groups="purchase.group_purchase_manager", default=_default_Ccurrency)

    @api.multi
    def cost_compute(self, price_type, uom=False, currency=False, company=False):

        if not currency and self._context.get('currency'):
            currency = self.env['res.currency'].browse(self._context['currency'])

        templates = self.with_context(currency=False)
        cost = super(ProductTemplateCost, templates).cost_compute(price_type, uom, currency=False,  company=company)
        if price_type in ['product_cost', 'product_cost']:  
            for template in self:

                cost[template.id] = template.cost_currency_id.compute(cost[template.id],
                                                                         currency or template.currency_id, round=False)
        return cost

        

class ProductProductcost(models.Model):
    _inherit = 'product.product'


    @api.multi
    def cost_compute(self, price_type, uom=False, currency=False, company=False):

        if not currency and self._context.get('currency'):
            currency = self.env['res.currency'].browse(self._context['currency'])

        templates = self.with_context(currency=False)
        cost = super(ProductTemplateCost, templates).cost_compute(price_type, uom, currency=False,  company=company)
        if price_type in ['product_cost', 'product_cost']:  
            for template in self:

                cost[template.id] = template.cost_currency_id.compute(cost[template.id],
                                                                         currency or template.currency_id, round=False)
        return cost

