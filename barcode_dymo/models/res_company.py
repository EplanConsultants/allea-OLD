from odoo import fields, models


class Company(models.Model):
    _inherit = 'res.company'

    barcode_logo = fields.Image(string="Barcode logo")
