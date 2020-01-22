from django.urls import path, include
from . import views as admin_views

urlpatterns = [
    path('dashboard/', admin_views.dashboard , name='admin-dashboard'),
    path('farmers/', admin_views.farmers , name='admin-farmers'),
    path('buyers/', admin_views.buyers , name='admin-buyers'),
    path('services/', admin_views.services , name='admin-services'),
    path('revenue/', admin_views.revenue , name='admin-revenue'),
]