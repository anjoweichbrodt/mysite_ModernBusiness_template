"""conservation_weichbrodt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path


from mysite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('404/', views.fourOfour, name='404'),
    path('about/', views.about, name='about'),
    path('blog-home-1/', views.blog1, name='blog-home-1'),
    path('blog-home-2/', views.blog2, name='blog-home-2'),
    path('blog-post/', views.blogpost, name='blog-post'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('portfolio-1-col/', views.portfolio1, name='portfolio-1-col'),
    path('portfolio-2-col/', views.portfolio2, name='portfolio-2-col'),
    path('portfolio-3-col/', views.portfolio3, name='portfolio-3-col'),
    path('portfolio-4-col/', views.portfolio4, name='portfolio-4-col'),
    path('pricing/', views.pricing, name='pricing'),
    path('services/', views.services, name='services'),
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),
    path('sidebar/', views.sidebar, name='sidebar'),
    path('base/', views.base, name='base'),
    path('portfolio-item/', views.portfolio_item, name='portfolio-item'),

]