
from odoo import models, fields, api, _
import odoo.addons.decimal_precision as dp
from odoo.exceptions import   UserError, RedirectWarning




class ProductProductCost(models.Model):
    _inherit = 'product.product'


    @api.multi
    def cost_compute(self, price_type, uom=False, currency=False, company=False):

        if not currency and self._context.get('currency'):
            currency = self.env['res.currency'].browse(self._context['currency'])

        templates = self.with_context(currency=False)
        cost = super(ProductTemplateCost, templates).cost_compute(price_type, uom, currency=False,  company=company)
        if price_type in ['product_cost', 'product_cost']:  
            for template in self:

                cost[template.id] = template.cost_currency_id.compute(cost[template.id], currency or template.currency_id, round=False)
        return cost