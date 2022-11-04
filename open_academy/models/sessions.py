# -*- coding: utf-8 -*-

# from email.policy import default
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


class Session(models.Model):
    _name = 'open_academy.session'
    _description = 'Session'

    def __instructor_id_domain(self):
        category_id_ref = self.env.ref('open_academy.res_partner_category_techlevel1').id
        #return [('category_id', '=', category_id_ref)]
        return ['|',
              ('instructor', '=', True),
              '|',
              ('category_id', '=', category_id_ref),
              ('category_id', '=', 'res_partner_category_techlevel2'),
              ]

    def __category_techlevel1(self):
        category_id_ref = api.Environment.ref('open_academy.res_partner_category_techlevel1').id
        return category_id_ref

    def __category_techlevel2(self):
        category_id_ref = self.env.ref('open_academy.res_partner_category_techlevel2').id
        return category_id_ref

    name = fields.Char(required=True)
    description = fields.Char()
    start_date = fields.Date(default=datetime.today())
    duration = fields.Integer()
    numder_of_seats = fields.Integer()
    instructor_id = fields.Many2one('res.partner', domain=['|', ('instructor', '=', True), '|', ('category_id.name', '=like', 'Level 1'), ('category_id.name', '=like', 'Level 2')])
    course_id = fields.Many2one('open_academy.course', required=True)
    percentage_of_seats = fields.Integer(compute='_compute_percentage_of_seats')
    active = fields.Boolean(default=True)
    attendes_ids = fields.Many2many('res.partner')

    _sql_constraints = [
        ('name_diff', 'CHECK (description <> name)', "The session name must be different from the description."),
        ('name_uniq', 'UNIQUE (name)', "The session name must be unique.")
    ]

    @api.depends('numder_of_seats', 'attendes_ids')
    def _compute_percentage_of_seats(self):
        for record in self:
            if record.numder_of_seats > 0:
                record.percentage_of_seats = len(record.attendes_ids)*(100/record.numder_of_seats)
            else:
                record.percentage_of_seats = 0
 
    @api.constrains('course_id', 'instructor_id')
    def _constrains_instructor_id(self):
        for record in self:
            if record.instructor_id.id > 0 and record.course_id.id > 0:
                if record.instructor_id in (record.course_id.attendes_ids):
                    raise ValidationError("The instructor should not be on the attendance list.")

