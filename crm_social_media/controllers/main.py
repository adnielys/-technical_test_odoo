# -*- coding: utf-8 -*-
from odoo import http, _
from odoo import tools
from odoo.http import request


class WebsiteCustomer(http.Controller):

    def _get_customer_search_domain(self, search):
        domain = []
        if search:
            search_terms = search.split(" ")
            domain = ['|', '|', '|']
            for term in search_terms:
                domain.append(('name', 'ilike', term))
                for social_field in ['facebook_url', 'linkedin_url', 'twitter_url']:
                    domain.append((social_field, 'ilike', term))

        return domain

    @http.route(['/customer-list', '/customer-list/page/<page>'], type='http', auth='public', website=True)
    def customer_list(self, page=0, search=''):

        domain = []
        if search:
            domain = self._get_customer_search_domain(search)

        total_partners = request.env['res.partner'].search_count(domain)

        pager = request.website.pager('/customer-list', total=total_partners, page=page, step=10, url_args=None)

        partners = request.env['res.partner'].search(domain, limit=10, offset=pager['offset'])

        return request.render('crm_social_media.website_customer_list', {
            'partners': partners,
            'pager': pager,
        })
