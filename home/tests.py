# home/tests.py

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import HomeHero, HomeStat, HomeIntro, HomeSkill, HomeService, HomeProcess, HomeTool, HomeFAQ, HomeCTA

class HomeApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.hero = HomeHero.objects.create(
            title="Capturing",
            typewriter_phrases="Cinematic Excellence,Visual Storytelling,Timeless Memories,Creative Vision,Artistic Narratives",
            subtitle="Transforming your precious moments into breathtaking visual stories through professional cinematography and creative excellence",
            video="intro.mp4",
            primary_button_text="Watch Portfolio Reel",
            secondary_button_text="View Our Work",
            is_active=True
        )
        self.stat = HomeStat.objects.create(
            name="Projects Completed",
            value="4M",  # Changed to alphanumeric value
            suffix="",  # Empty suffix since "M" is in value
            icon="Calendar",
            order=1,
            is_active=True
        )
        self.intro = HomeIntro.objects.create(
            title="Crafting Visual Stories That Inspire",
            subtitle="With over 8 years of experience in professional videography, I specialize in capturing the essence of life's most precious moments and transform into cinematic masterpieces.\nMy journey began with a simple camera and an insatiable curiosity for storytelling. Today, I've had the privilege of working with loving couples, businesses, and creators across the globe, helping them share their unique stories through the power of video.\nEvery project is an opportunity to push creative boundaries while delivering results that exceed expectations. I believe in the perfect blend of technical expertise and artistic vision.",
            image="videographerman.jpg",
            achievements="Vimeo Staff Pick Winner 2023,Wedding Wire Couples Choice Award,Featured in Canon Creator Showcase,Real Estate Marketing Award",
            primary_button_text="View My Portfolio",
            secondary_button_text="Contact Me",
            is_active=True
        )
        self.skill = HomeSkill.objects.create(
            title="Storytelling",
            description="Transforming ideas into compelling narratives.",
            icon="PenTool",
            order=1,
            is_active=True
        )
        self.service = HomeService.objects.create(
            title="Wedding Films",
            description="Capturing the magic of your special day with cinematic elegance and emotional depth.",
            icon="Film",
            order=1,
            is_active=True
        )
        self.process = HomeProcess.objects.create(
            title="Creative Planning",
            description="We brainstorm and conceptualize your story with detailed scripts and shot planning.",
            icon="PenTool",
            order=1,
            is_active=True
        )
        self.tool = HomeTool.objects.create(
            title="Software",
            description="Adobe Premiere Pro, DaVinci Resolve, After Effects",
            icon="Laptop",
            order=1,
            is_active=True
        )
        self.faq = HomeFAQ.objects.create(
            question="What working hours are manageable for you?",
            answer="I am flexible and available to work during standard business hours (9 AM - 5 PM PKT) or can accommodate evening and weekend schedules based on project needs. Let’s discuss your timeline!",
            order=1,
            is_active=True
        )
        self.cta = HomeCTA.objects.create(
            title="Ready to Start Your Project?",
            description="Let’s collaborate and bring your vision to life with cinematic excellence.",
            button_text="Contact Me",
            is_active=True
        )

    def test_home_hero_list(self):
        response = self.client.get('/home/hero/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Capturing")

    def test_home_stat_list(self):
        response = self.client.get('/home/stats/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Projects Completed")
        self.assertEqual(response.data[0]['value'], "4M")
        self.assertEqual(response.data[0]['suffix'], "")

    def test_home_intro_list(self):
        response = self.client.get('/home/intro/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Crafting Visual Stories That Inspire")

    def test_home_skill_list(self):
        response = self.client.get('/home/skills/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Storytelling")

    def test_home_service_list(self):
        response = self.client.get('/home/services/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Wedding Films")

    def test_home_process_list(self):
        response = self.client.get('/home/processes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Creative Planning")

    def test_home_tool_list(self):
        response = self.client.get('/home/tools/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Software")

    def test_home_faq_list(self):
        response = self.client.get('/home/faqs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['question'], "What working hours are manageable for you?")

    def test_home_cta_list(self):
        response = self.client.get('/home/cta/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Ready to Start Your Project?")

    def test_home_stat_invalid_value(self):
        # Note: This test assumes HomeStatViewSet is changed to ModelViewSet to allow POST requests.
        # If it remains ReadOnlyModelViewSet, this test will fail unless you create the object differently.
        data = {
            "name": "Invalid Stat",
            "value": "abc",  # Invalid value
            "suffix": "",
            "icon": "Calendar",
            "order": 2,
            "is_active": True
        }
        response = self.client.post('/home/stats/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Value must be a number optionally followed by 'M' or 'K'", str(response.data))

    def tearDown(self):
        self.hero.delete()
        self.stat.delete()
        self.intro.delete()
        self.skill.delete()
        self.service.delete()
        self.process.delete()
        self.tool.delete()
        self.faq.delete()
        self.cta.delete()