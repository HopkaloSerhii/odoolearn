# -*- coding: utf-8 -*-

from odoo import api, fields, models


class FillingSessions(models.TransientModel):
    _name = 'open_academy.filling_sessions'
    _description = 'Filling sessions'

    sessions_ids = fields.Many2many(comodel_name='open_academy.session', string='Sessions', default=lambda self: self.env.context["active_ids"])
    attendes_ids = fields.Many2many(comodel_name='res.partner', string='Attendes')
    

    def action_filling_sessions_apply(self):
        for session in self.sessions_ids:
            session.attendes_ids = self.attendes_ids
