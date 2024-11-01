"""
URL configuration for Hopsstar_engine project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from Hopsstar_app.sitemaps import StaticSitemap, NoteSitemap, CheatsheetSitemap, CareerSitemap
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static


sitemaps = {
    'static': StaticSitemap,
    'notes': NoteSitemap,
    'cheatsheets': CheatsheetSitemap,
    'careers': CareerSitemap,
}



urlpatterns = [
    path('admin/', include('admin_honeypot.urls')),
    path('', include('Hopsstar_app.urls')),
    path('Hopsstar@Admin-secret/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('pwa.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
