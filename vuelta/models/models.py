# -*- coding: utf-8 -*-

from odoo import models, fields, api


class vuelta(models.Model):
    _name = 'vuelta.vuelta'       
    _description = 'vuelta.vuelta'

    name = fields.Char()

    persona_id = fields.Many2one('vuelta.persona')
    #CREAR RELACION DE PERSONA ONETOMANY

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class persona(models.Model):
    _name = 'vuelta.persona'
    _description = 'vuelta.persona'

    nombre = fields.Char(string="Nombre")
    apellido1 = fields.Char(string="Primer Apellido")
    apellido2 = fields.Char(string="Segundo Apellido")
    vueltas_ids = fields.One2many('vuelta.vuelta', 'persona_id')
    nombreCompleto = fields.Char(compute="_nombreCompleto", store=True,string="Nombre Completo")
    etiqueta_ids = fields.Many2many('vuelta.etiqueta')
    imagen = fields.Image(string="Foto de perfil")

    @api.depends('nombre','apellido1','apellido2')
    def _nombreCompleto(self):
        for record in self:
            if (record.nombre and record.apellido1 and record.apellido2):
                record.nombreCompleto = record.nombre + ' '+record.apellido1+' '+record.apellido2 


    

class etiqueta(models.Model):
    _name = 'vuelta.etiqueta'

    nombre = fields.Char()