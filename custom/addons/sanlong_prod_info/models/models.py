from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class SanlongProdInfo(models.Model):
    _name = "sanlong.prod.info"
    _description = "sanlong prod info"
    _inherit = ["mail.thread", "mail.activity.mixin"]  # track_visibility

    mysql_id = fields.Integer("Mysql_id", required=True, readonly=True)
    slPN = fields.Char(string="品號", required=True, track_visibility="always")
    customPN = fields.Char(string="備註一", required=True, track_visibility="always")
    backPN = fields.Char(string="背番號", track_visibility="always")
    colorNO = fields.Char(string="色號/設備代號", track_visibility="always")
    mould = fields.Char(string="模具", track_visibility="always")
    standardSec = fields.Integer(string="標時", required=True, track_visibility="always")
    category = fields.Char(string="分類", track_visibility="always")
    TRDH_T_LINE = fields.Char(string="主要廠商", track_visibility="always")
    
    _sql_constraints = [
        ("mysql_id_uniq", "unique(mysql_id)", "mysql_id must be unique"),
    ]

