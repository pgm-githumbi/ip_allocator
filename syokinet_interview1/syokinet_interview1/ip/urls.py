
from django.urls import path, include, re_path

from . import views, models


allocated = models.AllocatedIpResource()
available = models.AvailableIpResource()
urlpatterns = [
    # Other URL patterns
    path('', include(allocated.urls), name='allocated'),
    path('allocate/', views.allocate_ip, name='allocate'),
    
    path('', include(available.urls), name='available'),
    path('release/<str:ip_address>/', views.release_ip, ),
]