# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class prova_magazzino(models.Model):
#     _name = 'prova_magazzino.prova_magazzino'
#     _description = 'prova_magazzino.prova_magazzino'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
