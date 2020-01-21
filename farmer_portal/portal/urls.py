from django.urls import path, include
from . import views as portal_views
from farmers import views as farmer_views


urlpatterns = [
    path('', portal_views.home , name='portal-home'),
    path('farmer/', include('farmers.urls')),
    path('service/', include('services.urls')),
    path('buyer/', include('buyer.urls')),
    path('admin_portal/', include('admin_portal.urls')),
<<<<<<< HEAD
=======
    path('login/', portal_views.login, name='login')
>>>>>>> 6b637f2839f8bed860549d1ea7cb25e4c278424f
]
