# -*- coding: utf-8 -*-
from odoo import models, fields

class Medicos(models.Model):
    _name = "sis.medicos"
    nombre = fields.Char(string='Nombre', required=True)
    primer_apellido = fields.Char(string='Primer Apellido', required=True)
    segundo_apellido = fields.Char(string='Segundo Apellido', required=True)
    foto = fields.Binary(string='Foto')
    edad = fields.Integer(string='Edad')
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento")
    genero = fields.Selection([('h', 'Hombre'), ('m', 'Mujer'), ('o', 'Otro')], string='Género')
    nacionalidad = fields.Many2one('sis.nacionalidades', string='Nacionalidad', ondelete='restrict')
    especialidad = fields.Many2one('sis.especialidades', 'Especialidad', ondelete='restrict')
    country_id = fields.Many2one('sis.paises', 'País', ondelete='restrict')

    def name_get(self):
        res = []
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res

Medicos()