import unittest
from unittest.mock import Mock

from odoo.tests.common import TransactionCase
from odoo.http import request
import werkzeug


class TestWebsiteCustomer(TransactionCase):
    def setUp(self):
        super().setUp()
        self.Partner = self.env['res.partner']
        self.partner1 = self.Partner.create({
            'name': 'Partner 1',
            'facebook_url': 'https://www.facebook.com/partner1',
        })
        self.partner2 = self.Partner.create({
            'name': 'Partner 2',
            'linkedin_url': 'https://www.linkedin.com/in/partner2',
            'twitter_url': 'https://twitter.com/partner234',
        })

    def test_customer_page_rendering(self):
        search_term = 'Partner 2',

        response = request.render(
            'crm_social_media.website_customer_list', {'search': search_term}
        )
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
