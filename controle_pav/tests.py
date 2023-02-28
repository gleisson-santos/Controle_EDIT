from django.contrib.auth import get_user_model, authenticate, login, logout, SESSION_KEY, get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.test import TestCase, RequestFactory
from django.urls import reverse
from .models import *
from .views import *
from datetime import date, datetime, time, timedelta
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import force_login 

class IndexViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='testuser@test.com', password='testpassword'
        )

    def test_index_view(self):
        url = reverse('index')
        request = self.factory.get(url)
        request.user = self.user
        response = index(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dados/index.html')
        self.assertIn('cadastro1', response.context)
        self.assertIn('esgoto21', response.context)
        self.assertIn('pavimento5', response.context)