from odoo import fields, models, api

class BrandExtend(models.Model):
    _name = 'brand_extend'
    name = fields.Char()
