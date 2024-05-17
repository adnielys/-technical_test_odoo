import unittest
from odoo import fields, models


class TestResPartner(unittest.TestCase):

    def setUp(self):
        self.Partner = self.env['res.partner']

    def test_social_media_fields(self):
        # Create a test partner record
        partner = self.Partner.create({
            'name': 'Test Partner',
            'facebook_url': 'https://www.facebook.com/testpartner',
            'linkedin_url': 'https://www.linkedin.com/in/testpartner',
            'twitter_url': 'https://twitter.com/testpartner123',
        })

        # Check if social media fields are correctly set
        self.assertEqual(partner.facebook_url, 'https://www.facebook.com/testpartner')
        self.assertEqual(partner.linkedin_url, 'https://www.linkedin.com/in/testpartner')
        self.assertEqual(partner.twitter_url, 'https://twitter.com/testpartner123')

        # Check if social media fields are of expected type (string)
        self.assertEqual(type(partner.facebook_url), str)
        self.assertEqual(type(partner.linkedin_url), str)
        self.assertEqual(type(partner.twitter_url), str)


if __name__ == '__main__':
    unittest.main()
