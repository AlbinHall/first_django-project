from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done_default_false(self):
        item = Item.objects.create(name="Test Todo Models")
        self.assertFalse(item.done)