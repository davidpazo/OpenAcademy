# -*- coding: utf-8 -*-

from openerp import models, fields, api

#Añadimos la clase session, que contiene el modelo de las sesiones
 class Course(models.Model):
      _name = 'openacademy.course'
  
      name = fields.Char(string="Titulo", required=True)
     description = fields.Text() 
     responsible_id = fields.Many2one('res.users',
         ondelete='set null', string="Responsable", index=True)
class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")

    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('openacademy.course',
        ondelete='cascade', string="Curso", required=True)