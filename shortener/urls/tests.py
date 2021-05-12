# from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from .models import Url 
from django.contrib.messages import get_messages


class TestBasicViews(TestCase):
    def setUp(self):
        Url.objects.create(long_url="http://google.com")

    c = Client()

    def test_home_get(self):
        
        response = self.c.get(reverse('urls-index'))
        assert "urls/index.html" in [t.name for t in response.templates]
    
    def test_home_post(self):
        response = self.c.post(reverse('urls-index'), {'long_url': 'dailymail.com'}, follow=True )
        url = Url.objects.get(long_url = 'http://dailymail.com' )
        self.assertRedirects(response, '/')
        message = list(response.context.get('messages'))[0]
        self.assertIn(url.short_url, str(message))

    

    def test_redirect(self):
        url = Url.objects.get(long_url="http://google.com")
        response = self.c.get(f'/{url.short_url}', follow=True)
        assert(response.redirect_chain[1])== ('http://google.com', 302)

    

      
       