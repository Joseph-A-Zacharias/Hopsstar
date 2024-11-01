from django.contrib import sitemaps
from django.urls import reverse
from .models import Note, Cheatsheet, Career


class StaticSitemap(sitemaps.Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['about', 'termsandprivacy', 'research']

    def location(self, item):
        return reverse(item)

class NoteSitemap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Note.objects.all()
    
    
class CheatsheetSitemap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Cheatsheet.objects.all()
      
class CareerSitemap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Career.objects.all()
   