# contact/management/commands/populate_contact.py

from django.core.management.base import BaseCommand
from contact.models import ContactInfo, WhyChooseUs, HeroSection


class Command(BaseCommand):
    help = 'Populate initial contact page data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating contact data...')
        
        # Create Contact Info
        contact_info_data = [
            {
                'icon': 'Phone',
                'title': 'Phone',
                'info': '+92 300 1234567',
                'link': 'tel:+923001234567',
                'order': 1
            },
            {
                'icon': 'Mail',
                'title': 'Email',
                'info': 'info@alexrodriguez.com',
                'link': 'mailto:info@alexrodriguez.com',
                'order': 2
            },
            {
                'icon': 'MapPin',
                'title': 'Location',
                'info': 'I-8, Islamabad, Pakistan',
                'link': '#map',
                'order': 3
            },
            {
                'icon': 'Clock',
                'title': 'Working Hours',
                'info': 'Mon - Sat: 9AM - 8PM',
                'link': '#',
                'order': 4
            },
        ]
        
        for info in contact_info_data:
            ContactInfo.objects.get_or_create(
                title=info['title'],
                defaults=info
            )
            self.stdout.write(self.style.SUCCESS(f'Created contact info: {info["title"]}'))
        
        # Create Why Choose Us
        reasons_data = [
            {
                'icon': 'Award',
                'title': 'Award Winning',
                'description': '15+ industry awards and recognition',
                'order': 1
            },
            {
                'icon': 'Star',
                'title': '500+ Projects',
                'description': 'Successfully delivered with excellence',
                'order': 2
            },
            {
                'icon': 'Heart',
                'title': '98% Satisfaction',
                'description': 'Happy clients who return',
                'order': 3
            },
            {
                'icon': 'Camera',
                'title': 'Premium Quality',
                'description': 'Cinema-grade equipment & expertise',
                'order': 4
            },
        ]
        
        for reason in reasons_data:
            WhyChooseUs.objects.get_or_create(
                title=reason['title'],
                defaults=reason
            )
            self.stdout.write(self.style.SUCCESS(f'Created reason: {reason["title"]}'))
        
        # Create Hero Section for Contact Page
        hero_data = {
            'page': 'contact',
            'title': 'Get in Touch',
            'subtitle': "Let's Create Something Extraordinary Together",
            'description': 'Have a project in mind? Let\'s discuss how we can bring your vision to life with our cinematic expertise.',
            'badge_text': 'We\'re Here to Help',
            'badge_icon': 'MessageSquare',
            'media_type': 'video',
        }
        
        hero, created = HeroSection.objects.get_or_create(
            page='contact',
            defaults=hero_data
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('Created hero section for contact page'))
        else:
            self.stdout.write(self.style.WARNING('Hero section for contact page already exists'))
        
        self.stdout.write(self.style.SUCCESS('Contact data population completed!'))