# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Clientes(models.Model):
     _name = 'clientes.clientes'
     _description = 'clientes.clientes'

     nombre = fields.Char()
     apellido = fields.Char(string='Primer Apellido')
     apellido2 = fields.Char(string='Segundo Apellido')
     descripcion = fields.Text()
     telefono = fields.Integer()
     fecha_nacimiento = fields.Date()
     activo = fields.Boolean()
     puesto_id = fields.Many2one('clientes.puesto')
     renta_id = fields.Many2one('clientes.renta')

class Renta(models.Model):
     _name = 'clientes.renta'
     _description = 'clientes.renta'

     codigo = fields.Char()
     ano = fields.Integer(string='Año')
     descripcion = fields.Char()
     clientes_id = fields.One2many('clientes.clientes', 'renta_id')


class Puesto(models.Model):

    _name = 'clientes.puesto'
    _description = 'Tipo puesto trabajo'
    
    nombre = fields.Char()
    descripcion = fields.Char()
    clientes_id = fields.One2many('clientes.clientes', 'puesto_id')



