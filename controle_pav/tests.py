from email import contentmanager
from ssl import HAS_TLSv1_1
from django.test import TestCase

# Create your tests here.
from django.test import TestCase, RequestFactory
from controle_pav.views import index

from django.test import TestCase, RequestFactory
from django.urls import reverse
from myapp.views import index

class IndexViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index_view(self):
        url = reverse('index')
        request = self.factory.get(url)
        response = index(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dados/index.html')
        self.assertIn('cadastro1', response.context)
        self.assertIn('esgoto21', response.context)
        self.assertIn('pavimento5', response.context)
