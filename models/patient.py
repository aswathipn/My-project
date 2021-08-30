# -*- coding: utf-8 -*-
import datetime
from odoo import api, fields, models, _


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _rec_name = 'reference_no'
    _description = "Hospital Patient"

    name_id = fields.Many2one('res.partner', string="Name")
    reference_no = fields.Char(string='Order Reference', required=True,
                               copy=False,
                               readonly=True, default=lambda self: _('New'))
    bdate = fields.Date(string='DOB', related='name_id.dob')
    age = fields.Char(string="Age", compute='_compute_age')
    mobile = fields.Char(string='Mobile', related='name_id.mobile')
    phone = fields.Char(string='Phone', related='name_id.phone')
    #address = fields.Many2one('res.partner', string='Adress', related='name_id',
    #          domain="['|', ('street', '=', street), ('state_id', '=', state_id), ('country_id', '=', country_id)]",)
    gender = fields.Selection([
        ('other', 'Other'),
        ('male', 'Male'),
        ('female', 'Female'),
    ], srting='Gender', default='other')
    bloodgrp = fields.Selection([
        ('a+', 'A+'),
        ('b+', 'B+'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
        ('o+', 'O+'),
        ('o-', 'O-'),
    ], string="Blood Group")
    note = fields.Text(string='Note')

    @api.depends("bdate")
    def _compute_age(self):
        today_date = datetime.date.today()
        for pat in self:
            if pat.bdate:
                bdate = fields.Datetime.to_datetime(pat.bdate).date()
                total_age = str(int((today_date - bdate).days / 365))
                pat.age = total_age
            else:
                pat.age = "..."

    @api.model
    def create(self, vals):
        if vals.get('note'):
            vals['note'] = 'New Patient'
        if vals.get('reference_no', _('New')) == _('New'):
            vals['reference_no'] = self.env['ir.sequence'].next_by_code(
                'hospital.patient') or _('New')
        res = super(HospitalPatient, self).create(vals)
        return res
