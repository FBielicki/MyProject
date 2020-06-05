"""Tests for users app."""

from django.test import TestCase

from models import User


class UserTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.credentials = {
            'username': 'testuser',
            'password': 'secret',
        }
        User.objects.create_user(**self.credentials)

    def test_successful_login(self):
        # POST credentials.
        response = self.client.post('/login/', self.credentials, follow=True)

        # Should be logged in.
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_active)

    def test_wrong_password_login(self):
        # POST credentials.
        response = self.client.post(
            '/login/',
            {
                'username': 'testuser',
                'password': 'wrong_password',
            },
            follow=True,
        )

        # Should not be logged in.
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_active)

    def test_wrong_username_login(self):
        # POST credentials.
        response = self.client.post(
            '/login/',
            {
                'username': 'wrong_username',
                'password': 'secret',
            },
            follow=True,
        )

        # Should not be logged in.
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_active)

    def test_logout(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)

        response = self.client.post(
            '/logout/',
            follow=True,
        )
        self.assertFalse(response.context['user'].is_active)
