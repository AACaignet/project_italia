# -*- coding:utf-8 -*-

from odoo import fields, models, api

class PorductoMagazzino(models.Model):
    _inherit = 'product.template'


    brand_id = fields.Many2one(
        comodel_name='product.template',
        string='Brand',
        ondelete='cascade')


    Stagione = fields.Selection(selection=[
        ('Primavera', 'Primavera'),
        ('Estate', 'Estate'),
        ('Autunno', 'Autunno'),
        ('Inverno', 'Inverno'),
    ], string='Stagione')


