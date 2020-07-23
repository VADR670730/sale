# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sale_order_template_child_id = fields.Many2one(
        comodel_name='sale.order.template.child', 
        string='Order template child'
    )                                                                                                                                                   