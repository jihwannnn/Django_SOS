from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class AuthTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'testuser'
        self.password = 'testpassword123'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_view(self):
        response = self.client.get(reverse('question:index'))
        self.assertEqual(response.status_code, 200)
        
        login_data = {
            'username': self.username,
            'password': self.password,
        }
        response = self.client.post(reverse('question:index'), data=login_data)
        self.assertEqual(response.status_code, 302)  # Redirects to 'question:main'
        self.assertRedirects(response, reverse('question:main'))

        # Check if the user is authenticated
        user = response.wsgi_request.user
        self.assertTrue(user.is_authenticated)
        
    def test_login_invalid_credentials(self):
        login_data = {
            'username': self.username,
            'password': 'wrongpassword',
        }
        response = self.client.post(reverse('question:index'), data=login_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid credentials')
        
        # Check if the user is not authenticated
        user = response.wsgi_request.user
        self.assertFalse(user.is_authenticated)

    def test_logout_view(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('question:logout'))
        self.assertEqual(response.status_code, 302)  # Redirects to 'question:index'
        self.assertRedirects(response, reverse('question:index'))
        
        # Check if the user is logged out
        user = response.wsgi_request.user
        self.assertFalse(user.is_authenticated)

    def test_signup_view(self):
        signup_data = {
            'username': 'newuser',
            'password': 'newpassword123',
            'password_confirm': 'newpassword123',
        }
        response = self.client.post(reverse('question:signup'), data=signup_data)
        self.assertEqual(response.status_code, 302)  # Redirects to 'question:index'
        self.assertRedirects(response, reverse('question:index'))
        
        # Check if the new user is created and authenticated
        user = User.objects.get(username='newuser')
        self.assertIsNotNone(user)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_signup_password_mismatch(self):
        signup_data = {
            'username': 'newuser',
            'password': 'newpassword123',
            'password_confirm': 'differentpassword',
        }
        response = self.client.post(reverse('question:signup'), data=signup_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Passwords do not match')
        
        # Check if the user is not created
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username='newuser')
