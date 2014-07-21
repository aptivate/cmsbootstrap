from django.core.management import call_command
from django.test import TestCase

class SimpleTest(TestCase):
    fixtures = ['homepage']

    def test_get_homepage(self):
        """
        Test that we can download and render the fixture home page correctly.
        This requires that django-cms isn't broken by installing this module.
        """

        response = self.client.get('/en/')
        self.assertContains(response, 'CMSBootstrap')
