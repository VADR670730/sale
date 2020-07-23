# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'                                
   
    @api.model    
    def cron_action_orders_free_auto_invoiced(self):
        sale_order_ids = self.env['sale.order'].search(
            [
                ('amount_total', '=', 0),
                ('invoice_status', '=', 'to invoice')
            ]
        )
        if sale_order_ids:
            for sale_order_id in sale_order_ids:
                # order_line
                for order_line_item in sale_order_id.order_line:
                    order_line_item.invoice_status = 'no'
                # invoice_status
                sale_order_id.invoice_status = 'no'                                                                                          