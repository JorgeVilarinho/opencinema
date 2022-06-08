# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Films(models.Model):
    _name = 'opencinema.film'
    _description = 'Open Cinema Films'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    release_date = fields.Date(required=True)
    year = fields.Char(required=True)
    duration = fields.Integer()
    director = fields.Many2one('opencinema.director', 
        ondelete="set null", index=True)

class Screening(models.Model):
    _name = 'opencinema.screening'
    _description = 'Open Cinema Screenings'

    place = fields.Char(required = True)
    screening_date = fields.Date()
    seats = fields.Integer(string="Number of seats")
    price = fields.Float(digits=(6, 2), help="The price for the movie")
    responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)

class Director(models.Model):
    _name = 'opencinema.director'
    _description = 'Open Cinema Directors'

    name = fields.Char(required=True)
    nacionality = fields.Char(required=True)
    films = fields.One2many('opencinema.film', 'director', string="Films")
