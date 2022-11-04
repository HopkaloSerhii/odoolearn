# -*- coding: utf-8 -*-

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(string="Instructor", default=False)
    session_ids = fields.Many2many('open_academy.session')
