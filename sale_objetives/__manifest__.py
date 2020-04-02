# -*- coding: utf-8 -*-
{
    'name': 'Sale Objetives',
    'version': '10.0.1.0.0',    
    'author': 'Odoo Nodriza Tech (ONT)',
    'website': 'https://nodrizatech.com/',
    'category': 'Tools',
    'license': 'AGPL-3',
    'depends': ['base', 'sale'],
    'data': [        
        'security/ir.model.access.csv',
        'views/sale_objetives.xml',
    ],
    'installable': True,
    'auto_install': False,    
}