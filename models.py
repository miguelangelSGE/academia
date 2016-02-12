# -*- coding: utf-8 -*-

from openerp import models, fields

class academia(models.Model):
    _name = 'academia.cursos'
    
    nombre = fields.Char(string = "Titulo del curso",required=True)
    descripcion = fields.Char(string = "Descripcion del curso")
    fechaInicio = fields.Date(string = "Fecha de inicio")
    turno = fields.Selection([("1","Mañana"),("2","Tarde")])