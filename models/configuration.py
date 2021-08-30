# -*- coding: utf-8 -*-
import datetime
from odoo import api, fields, models, _


class HospitalDisease(models.Model):
    _name = "hospital.disease"
    _rec_name = 'disease'
    _description = "Hospital Disease"

    disease = fields.Char(string='Name', required=True)
    type = fields.selection([
        ('fever', 'Fever'),
        ('itching', 'Itching'),
        ('pain', 'Pain'),
    ])
