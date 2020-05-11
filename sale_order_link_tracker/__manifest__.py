# -*- coding: utf-8 -*-
{
    'name': 'Sale Order Link Tracker',
    'version': '12.0.1.0.0',    
    'author': 'Odoo Nodriza Tech (ONT)',
    'website': 'https://nodrizatech.com/',
    'category': 'Tools',
    'license': 'AGPL-3',
    'depends': ['base', 'sale', 'link_tracker'],
    'data': [
        'data/ir_cron.xml',
    ],
    'installable': True,
    'auto_install': False,    
}