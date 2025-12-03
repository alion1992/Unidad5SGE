# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Renta(models.Model):
    _name = 'renta.renta'
    _description = 'renta.renta'

    codigo = fields.Char()
    ano = fields.Integer()
    descripcion = fields.Char()

class Cliente(models.Model):
    _name = 'renta.cliente'
    _description = 'renta.cliente'

    nombre = fields.Char()
    apellido1 = fields.Char()
    apellido2 = fields.Char()
