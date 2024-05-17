# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class Customer(models.Model):
    _inherit = 'res.partner'

    facebook_url = fields.Char('Facebook')
    linkedin_url = fields.Char('Linkedin')
    twitter_url = fields.Char('Twitter')

    full_profile = fields.Boolean('Full profile', default=False, compute='_compute_full_profile',
                                  search='_search_full_profile')

    @api.depends('facebook_url', 'linkedin_url', 'twitter_url')
    def _compute_full_profile(self):
        for record in self:
            record.full_profile = False
            if record.facebook_url and record.linkedin_url and record.twitter_url:
                record.full_profile = True

    def _search_full_profile(self, operator, value):
        if operator not in ['=', '!='] or not isinstance(value, bool):
            raise UserError(_('Operation not supported'))
        partner = self.env['res.partner']
        match value:
            case True:
                domain = []
                if operator == '=':
                    domain.append(('facebook_url', operator, value), ('linkedin_url', operator, value),
                                  ('twitter_url', operator, value))
                else:
                    domain.append('|', '|', ('facebook_url', operator, value), ('linkedin_url', operator, value),
                                  ('twitter_url', operator, value))

                partner = self.env['res.partner'].search(domain)
            case _:
                partner = self.env['res.partner'].search(
                    ['|', '|', ('facebook_url', operator, value), ('facebook_url', operator, value),
                     ('facebook_url', operator, value)])
        return [('id', 'in', partner.ids)]



