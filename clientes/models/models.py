# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Clientes(models.Model):
     _name = 'clientes.clientes'
     _description = 'clientes.clientes'

     nombre = fields.Char()
     apellido = fields.Char()
     descripcion = fields.Text()

class Puesto(models.Model):

    _name = 'clientes.puesto'
    _description = 'tipo puesto trabajo'

    descripcion = fields.Char()



