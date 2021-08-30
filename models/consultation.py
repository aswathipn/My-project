# -*- coding: utf-8 -*-
import datetime
from odoo import api, fields, models, _


class HospitalConsultation(models.Model):
    _name = "hospital.consultation"
    #_rec_name = 'ticket_no'
    _description = "Hospital consultation"

    consultation_no = fields.Char(string='Consultation', required=True,
                            copy=False,
                            readonly=True, default=lambda self: _('New'))
    patient_card = fields.Many2one('hospital.patient', string='Patient Card')
    date = fields.Datetime(string='Date&Time')
    doctor_id = fields.Many2one('res.partner', string='Doctor',
                domain="[('function', '=', 'doctor')]",)
    department = fields.Many2one('res.partner', string="Department")
    disease = fields.Many2one('hospital.consultation', string='Disease')
    type = fields.Selection([
        ('op', 'OP'),
        ('ip', 'IP'),
    ], srting='Consultation Type', default='op')
    state = fields.Selection([('draft', 'Draft'), ('op', 'OP'),
             ('cancel', 'Cancelled'),
    ], string='Status', default='draft')
    note = fields.Text(string='Diagnose')

    # def action_confirm(self):
    #  self.state = 'op'
    #
    # def action_cancel(self):
    #     self.state = 'cancel'
    @api.model
    def create(self, vals):
        if vals.get('note'):
            vals['note'] = 'New Patient'
        if vals.get('ticket_no', _('New')) == _('New'):
            vals['ticket_no'] = self.env['ir.sequence'].next_by_code(
                'hospital.ticket') or _('New')
        res = super(HospitalTicket, self).create(vals)
        return res
