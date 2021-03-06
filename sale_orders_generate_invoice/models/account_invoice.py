# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def action_auto_create(self):
        return True

    @api.multi
    def action_auto_open(self):
        return True
