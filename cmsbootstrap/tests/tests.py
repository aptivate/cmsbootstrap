from django.core.management import call_command
from django.test import TestCase

class SimpleTest(TestCase):
    def test_get_homepage(self):
        """
        Test that we can download and render the fixture home page correctly.
        This requires that django-cms isn't broken by installing this module.
        """

        call_command('migrate')
        call_command('loaddata', 'homepage')
        response = self.client.get('/')
        self.assertContains(response, 'CMSBootstrap')
