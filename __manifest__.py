# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Hospital',
    'version' : '1.0',
    'summary': 'Hospital Management',
    'sequence': -100,
    'description': """ hospital management""",
    'category': '',
    'website': 'https://www.odoo.com/page/billing',
    'depends': ['contacts'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/patient.xml',
        'views/ticket.xml',
        'views/date.xml',
        'views/consultation.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
