# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import SUPERUSER_ID
from openerp import tools
from openerp.osv import osv, fields, expression
from openerp.tools.translate import _
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT
import openerp.addons.decimal_precision as dp
from openerp.tools.float_utils import float_round, float_compare

# Python
import psycopg2
import logging
_logger = logging.getLogger(__name__)


class sale_order_ckl(osv.Model):

    _inherit = 'sale.order'
    _description = 'Add fields and methods in sale.order'
    
    # 20/07/2015 (felix) Metodo original modificado
    def action_button_confirm(self, cr, uid, ids, context=None):
    
        # 20/07/2015 (felix) Verificar si existen productos hibridos
        for i in self.browse(cr, uid, ids, context):
            for line in i.order_line:
                if line.product_id.is_hybrid == True:
                    raise osv.except_osv('Advertencia','La cotizacion contiene productos que no pueden ser vendidos')
                    return {}
    
        assert len(ids) == 1, 'This option should only be used for a single id at a time.'
        self.signal_workflow(cr, uid, ids, 'order_confirm')
        return True
    
sale_order_ckl()
