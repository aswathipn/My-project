# -*- coding: utf-8 -*-
import datetime
from odoo import api, fields, models, _

class HospitalHistory(models.Model):
    _name = "hospital.history"
    _rec_name = 'ticket_no'
    _description = "Hospital History"

    ticket_no = fields.Char(string='OP Ticket', required=True,
                               copy=False,
                               readonly=True, default=lambda self: _('New'))

    #address = fields.Char(string='Address', related='name_id.street')
    date = fields.Datetime(string='Date&Time')
    doctor_id = fields.Many2one('res.partner', string='Doctor',
                domain="[('function', '=', 'doctor')]",)
    department = fields.Many2one('hospital.consultation', string='Department')

class HospitalTicket(models.Model):
    _name = "hospital.ticket"
    _rec_name = 'ticket_no'
    _description = "Hospital ticket"

    ticket_no = fields.Char(string='OP Ticket', required=True,
                               copy=False,
                               readonly=True, default=lambda self: _('New'))
    patient_card = fields.Many2one('hospital.patient', string='Patient Card')
    name_id = fields.Many2one(string="Name", related='patient_card.name_id')
    age = fields.Char(string="Age", related='patient_card.age')
    mobile = fields.Char(string='Mobile', related='name_id.mobile')
    phone = fields.Char(string='Phone', related='name_id.phone')
    #address = fields.Char(string='Address', related='name_id.street')
    date = fields.Datetime(string='Date&Time')
    doctor_id = fields.Many2one('res.partner', string='Doctor',
                domain="[('function', '=', 'doctor')]",)
    currency_id = fields.Many2one('res.currency', string="Currency")
    fee = fields.Monetary(string='Fee')
    gender = fields.Selection([
        ('other', 'Other'),
        ('male', 'Male'),
        ('female', 'Female'),
    ], srting='Gender', default='other', related='patient_card.gender')
    bloodgrp = fields.Selection([
        ('a+', 'A+'),
        ('b+', 'B+'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
        ('o+', 'O+'),
        ('o-', 'O-'),
    ], string="Blood Group", related='patient_card.bloodgrp')
    state = fields.Selection([('draft', 'Draft'), ('op', 'OP'),
             ('cancel', 'Cancelled'),
    ], string='Status', default='draft')


    def action_confirm(self):
     self.state = 'op'

    def action_cancel(self):
        self.state = 'cancel'
    @api.model
    def create(self, vals):
        if vals.get('note'):
            vals['note'] = 'New Patient'
        if vals.get('ticket_no', _('New')) == _('New'):
            vals['ticket_no'] = self.env['ir.sequence'].next_by_code(
                'hospital.ticket') or _('New')
        res = super(HospitalTicket, self).create(vals)
        return res
