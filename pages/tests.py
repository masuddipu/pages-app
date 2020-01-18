from django.test import SimpleTestCase

# Create your tests here.
class SimpleTests(SimpleTestCase):
    def home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)