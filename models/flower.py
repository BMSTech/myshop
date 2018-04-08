# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from odoo.tools.translate import _


class Flower(models.Model):
    _name = 'myshop.flower'

    name = fields.Char("Flower name")
    amount = fields.Integer()
    color = fields.Selection([('red', 'Red'), ('yellow', 'Yellow'), ('green','Green')])
    description = fields.Text()
    note = fields.Text()

    _sql_constraints = [
        ('unique_name', 'unique(name)', _('Flower name already exists, please try again!')),
    ]

    @api.constrains("amount")
    def _amount_validate(self):
        for flower in self:
            if flower.amount < 0:
                raise exceptions.ValidationError(_("Amount can't be less than zero"))