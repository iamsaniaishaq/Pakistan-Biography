"""
URL configuration for pkbio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from biography.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', prime_ministers_list, name='prime_ministers_list'),
    path('prime-minister/<int:pk>/', prime_minister_detail, name='prime_minister_detail'),
    path('add/', add_prime_minister, name='add_prime_minister'),
    path('edit/<int:pk>/', edit_prime_minister, name='edit_prime_minister'),
    path('delete/<int:pk>/', delete_prime_minister, name='delete_prime_minister'),
    path('api/prime-ministers/', PrimeMinistersListView.as_view(), name='prime_ministers_api'),
    path('api/prime-minister/<int:id>/', PrimeMinisterDetailView.as_view(), name='prime-minister-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)