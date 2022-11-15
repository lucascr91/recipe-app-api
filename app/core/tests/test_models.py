'''
Tests for models
'''
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

def create_user(**params):
    '''Helper function to create a user'''
    return get_user_model().objects.create_user(**params)

class ModelTests(TestCase):
    ''' Test for models '''

    def test_create_user_with_email_successful(self):
        '''Test creating a new user with an email is successful'''
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        '''Test the email for a new user is normalized'''
        sample_emails = [
            ['test1@EXAMPLE.COM', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(
                email=email,
                password='testpass123'
            )
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        '''Test creating user with no email raises error'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testpass123')

    def test_create_new_superuser(self):
        '''Test creating a new superuser'''
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'testpass123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        '''Test creating a recipe'''
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123',
        )
        recipe = models.Recipe.objects.create(
            user=user,
            title='Sample recipe name',
            time_minutes=5,
            price=Decimal('5.50'),
            description='Sample description'
        )

        self.assertEqual(str(recipe), recipe.title)


    def test_create_tag(self):
        '''Test creating a tag'''
        tag = models.Tag.objects.create(
            user=create_user(email='user@example.com', password='password123'),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)