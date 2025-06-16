from odoo import models, fields

class Cat(models.Model):
    _name = 'animals.cat'  # This defines the technical model name
    _description = 'Cat'