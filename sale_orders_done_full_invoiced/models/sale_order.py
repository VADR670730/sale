# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'
                                
    @api.model    
    def cron_sale_orders_done_full_invoiced(self):
        sale_order_ids = self.env['sale.order'].search(
            [
                ('state', '=', 'sale'),
                ('invoice_status', '=', 'invoiced')
            ]
        )
        if sale_order_ids:
            for sale_order_id in sale_order_ids:
                sale_order_id.state = 'done'    