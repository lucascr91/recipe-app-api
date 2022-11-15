'''
Tests for recipe APIs
'''
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Recipe

from recipe.serializers import RecipeSerializer


def create_recipe(user, **params):
    '''Helper function to create a recipe'''
    defaults = {
        'title': 'Sample recipe',
        'time_minutes': 10,
        'price': Decimal('5.00')
    }
    defaults.update(params)

    return Recipe.objects.create(user=user, **defaults)