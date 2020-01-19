from django.urls import path, include
from . import views as portal_views
from farmers import views as farmer_views


urlpatterns = [
    path('', portal_views.home , name='portal-home'),
    path('farmer/', include('farmers.urls')),
    path('buyer/', include('buyer.urls')),
    path('admin_portal/', include('admin_portal.urls')),
]
