# Client is like a browser client, to simulate requests
from django.test import TestCase, Client
from django.urls import reverse


class IndexViewTestCase(TestCase):

    # Creaates a client to initialize test
    def setUp(self):
        self.client = Client()
        self.url = reverse('index')
    
    # Destroy test
    def tearDown(self):
        pass

    # This function make a request to root page ('/') and test if the status code was succesful
    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    # Tests if index.html template is being used correctly
    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'index.html')