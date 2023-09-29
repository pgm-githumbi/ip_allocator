
from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('ip/allocate', views.allocate_ip, name='allocate_ip'),
]