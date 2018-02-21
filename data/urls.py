"""globalcitydata URL Configuration

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
from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'data'

urlpatterns = [
    path('collaborators/', TemplateView.as_view(template_name='data/staticpage/collaborators.html'), name='collaborators'),
    path('publications/', TemplateView.as_view(template_name='data/staticpage/publications.html'), name='publications'),
    path('submit-data/', views.submitDatasetView, name='submitDataset'),
    path('success/', views.successView, name='success'),
    path('<str:slug>/', views.detailView, name='detail'),  # Dataset Detail view
    # Must be last
    path('', views.homeView, name='home'), # Home View
]
