# -*- coding: utf-8 -*-

from odoo import models, fields


class Course(models.Model):
    _name = 'open_academy.course'
    _description = 'Open academy courses'
    _rec_name = "title"

    title = fields.Char(required=True)
    description = fields.Text()
    responsible_user_id = fields.Many2one('res.users', ondelete='restrict')
    sessions_ids = fields.One2many('open_academy.session', 'course_id')
