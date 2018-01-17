from django.test import TestCase, Client
from django.urls import reverse
from . import views

# Create your tests here.
class HomeViewTests(TestCase):

    def test_can_get_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_can_get_to_tournaments(self):
        response = self.client.get('/tournaments/')
        self.assertEqual(response.status_code, 200)

