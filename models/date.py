# -*- coding: utf-8 -*-
from odoo import api, fields, models


class BirthDate(models.Model):
    _inherit = "res.partner"

    dob = fields.Date(string="DOB")

