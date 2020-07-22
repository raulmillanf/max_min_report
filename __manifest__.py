# -*- coding: utf-8 -*-
{
    'name': "max_min_report",

    'summary': "Reporte que arroja todos los máximos y mínimos de los productos",

   
    'author': "Raúl Millán",
    
    'category': 'reportes',
    'version': '11.0.1',

  
    'depends': ['base','product','stock','product_brand'],

   
    'data': [
        'security/ir.model.access.csv',
        'views/stock_warehouse.xml',
        'views/max_min_report.xml',
        'views/product_cost_view.xml',
    ],
   "active": False,
    "installable": True,
}