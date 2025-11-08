# portfolio/tests.py

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import PortfolioCategory, Project
import json

class PortfolioApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = PortfolioCategory.objects.create(name="Wedding", icon="Heart", count=5, order=1, is_active=True)
        
        self.project = Project.objects.create(
            title="Test Project", category=self.category, thumbnail="test.jpg", video="test.mp4",
            description="Test description", views="5K", likes="1K", order=1, is_active=True
        )

    def test_portfolio_category_list(self):
        response = self.client.get('/portfolio/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Wedding")

    def test_project_list(self):
        response = self.client.get('/portfolio/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Test Project")

    def tearDown(self):
        self.category.delete()
        self.hero_slide.delete()
        self.project.delete()