from django.test import TestCase
from .models import Item
# Create your tests here.


class TestViews(TestCase):

    def test_get_todo_list(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/todo_list.html")

    def test_get_add_item_page(self):
        response = self.client.get("/add")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/add_item.html")

    def test_edit_item_page(self):
        item = Item.objects.create(name="Test Todo Item")
        response = self.client.get(f"/edit/{item.id}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/edit_item.html")

    def test_if_add_item_function_works(self):
        response = self.client.post("/add", {"name": "Test Add Item"})
        self.assertRedirects(response, "/")

    def test_if_delete_works(self):
        item = Item.objects.create(name="Test Todo Item")
        response = self.client.get(f"/delete/{item.id}")
        self.assertRedirects(response, "/")
        existing_item = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_item), 0)

    def test_toggle_function(self):
        item = Item.objects.create(name="Test Todo Item", done=True)
        response = self.client.get(f"/toggle/{item.id}")
        self.assertRedirects(response, "/")
        update_item = Item.objects.get(id=item.id)
        self.assertFalse(update_item.done)