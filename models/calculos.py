# -*- coding: utf-8 -*-
from odoo import models, fields, api

class calculos(models.Model):
    _name = "sis.calculos"
    peso = fields.Integer(string='Peso')
    altura = fields.Float(string='Altura')
    imc = fields.Char(string='IMC', compute='_calcularIMC')

    @api.one
    @api.depends('peso', 'altura')
    def _calcularIMC(self):
        if (self.peso != 0 and self.altura != 0):
            c = (self.peso/(self.altura*2))
            if c >= 0 and c <= 15.99:
                self.imc = "Delgadez severa"
            elif c >= 16.00 and c <= 16.99:
                self.imc = "Delgadez moderada"
            elif c >= 17.00 and c <= 18.49:
                self.imc = "Delgadez leve"
            elif c >= 18.50 and c <= 24.99:
                self.imc = "Normal"
            elif c >= 25.00 and c <= 29.99:
                self.imc = "Sobrepeso"
            elif c >= 30.00 and c <= 34.99:
                self.imc = "obesidad leve"
            elif c >= 35.00 and c <= 39.00:
                self.imc = "obesidad media"
            elif c >= 40.00:
                self.imc = "obesidad morbida"