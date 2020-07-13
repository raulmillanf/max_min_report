# -*- coding: utf-8 -*-
from odoo.exceptions import   UserError, RedirectWarning
import odoo.addons.decimal_precision as dp
from odoo import models, fields, api

class MaxMinReport(models.Model):

    _inherit = 'stock.warehouse.orderpoint'
    _name = 'max_min_report'
    product_cost = fields.Float(string='Costo', digits=dp.get_precision('Product Price'),related="product_id.product_cost",  groups="purchase.group_purchase_manager" ,help = "Costo referencial del producto.")
    qty_available = fields.Float('Quantity On Hand', related="product_id.qty_available", search='_search_qty_available', digits=dp.get_precision('Product Unit of Measure'))