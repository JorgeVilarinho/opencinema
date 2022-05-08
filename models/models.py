# -*- coding: utf-8 -*-

from platform import release

from pkg_resources import require
from odoo import models, fields, api


class Films(models.Model):
    _name = 'opencinema.film'
    _description = 'Open Cinema Films'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    release_date = fields.Date(required=True)
    year = fields.Char(required=True)
    duration = fields.Integer()
