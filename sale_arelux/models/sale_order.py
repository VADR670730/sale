# -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)

from openerp import api, models, fields
from openerp.exceptions import Warning

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    opportunity_id = fields.Many2one(
        comodel_name='crm.lead', 
        string='Opportunity', 
        domain="[('type', '=', 'opportunity')]", 
        required=True
    )