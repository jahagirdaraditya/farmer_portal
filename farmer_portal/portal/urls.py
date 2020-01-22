from django.urls import path, include
from . import views as portal_views
from farmers import views as farmer_views


urlpatterns = [
    path('', portal_views.home , name='portal-home'),
    path('farmer/', include('farmers.urls')),
    path('fpo/', include('fpo.urls')),
    path('buyer/', include('buyer.urls')),
    path('admin_portal/', include('admin_portal.urls')),
    path('service/', include('services.urls')),
    path('buyer/', include('buyer.urls')),
    path('admin_portal/', include('admin_portal.urls')),
<<<<<<< HEAD
    path('login/', portal_views.login, name='login')
=======
    path('login/', portal_views.login, name='login'),
    path('translate/', portal_views.translate, name='translate'),


>>>>>>> 76c73be4168616b0ee8baf0b13fa9d1b1d6e7850
]
