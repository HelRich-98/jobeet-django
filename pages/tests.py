from django.test import TestCase
from django.urls import reverse, resolve

from .views import HomeView


class HomeViewTests(TestCase):
    def test_root_url_returns_200(self):
        url = reverse("index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        url = reverse("index")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "pages/index.html")

    def test_url_resolves_to_HomeView(self):
        resolver = resolve("/")
        self.assertIs(resolver.func.view_class, HomeView)

    def test_post_method_not_allowed(self):
        url = reverse("index")
        response = self.client.post(url)
        self.assertEqual(response.status_code, 405)

    def test_reverse_index_returns_root_path(self):
        self.assertEqual(reverse("index"), "/")
