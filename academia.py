# -*- coding: utf-8 -*-

from openerp import models, fields, api

class cursos(models.Model):
    _name = 'academia.cursos'
    
    @api.depends('alumnos')
    def calculacoste(self):
        for rec in self:
            rec.coste = float(self.alumnos * 100)
        #return float(self.alumnos * 100)
    
    nombre = fields.Char(string = "Titulo del curso",required=True)
    descripcion = fields.Text(string = "Descripcion del curso")
    fechaInicio = fields.Date(string = "Fecha de inicio")
    turno = fields.Selection([("1","Mañana"),("2","Tarde")])
    alumnos = fields.Integer(string = "Alumnos", default = 20)
    coste = fields.Float(compute = "calculacoste")