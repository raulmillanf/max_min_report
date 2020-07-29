# -*- coding: utf-8 -*-
#Created by Ramf

import odoo.addons.decimal_precision as dp
from odoo import fields, models, api

class MaxMinReport(models.Model):

    _inherit = 'stock.warehouse.orderpoint'
    

    product_cost = fields.Float('Costo', digits=dp.get_precision('Product Price'), related="product_id.product_cost",  groups="purchase.group_purchase_manager" ,help = "Costo referencial del producto.")
    qty_available = fields.Float('Cantidad a mano', related="product_id.qty_available", search='_search_qty_available', digits=dp.get_precision('Product Unit of Measure'))
    product_brand_id = fields.Char('Marca', related='product_id.product_brand_id.name', store=True)
    product_commer_id = fields.Char('Linea comercial', related='product_id.product_commer_id.name', store=True)
    cost_currency = fields.Char(' ', related='product_id.cost_currency.symbol')
    sellers_str = fields.Char('Proveedor', compute = "_get_seller_name", store=True)

    def _get_seller_name(self):
        for record in self:
            ids= record.product_id.seller_ids.name
            if ids:
                record.sellers_str = record.product_id.seller_ids.name[0]