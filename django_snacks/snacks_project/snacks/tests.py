from django.test import SimpleTestCase
from django.http import response
from django.urls import reverse

class SnacksTests(SimpleTestCase):
    def test_home_status(self):
        # Arrange
        url = reverse("home")
        response = self.client.get(url).status_code

        #Assert
        self.assertEqual(response, 200)

    def test_about_status(self):
        # Arrange
        url = reverse("about")
        response = self.client.get(url).status_code

        #Assert
        self.assertEqual(response, 200)

    def test_home_template(self):
        # Arrange
        url = reverse("home")
        response = self.client.get(url)

        #Assert
        self.assertTemplateUsed(response, "home.html")

    def test_about_template(self):
        # Arrange
        url = reverse("about")
        response = self.client.get(url)

        #Assert
        self.assertTemplateUsed(response, "about.html")    