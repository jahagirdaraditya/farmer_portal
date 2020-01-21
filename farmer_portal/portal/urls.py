from django.urls import path, include
from . import views as portal_views
from farmers import views as farmer_views


urlpatterns = [
    path('', portal_views.home , name='portal-home'),
    path('farmer/', include('farmers.urls')),
<<<<<<< HEAD
    path('service/', include('services.urls')),
=======
    path('buyer/', include('buyer.urls')),
    path('admin_portal/', include('admin_portal.urls')),
<<<<<<< HEAD
    path('login/', portal_views.login, name='login')
=======
>>>>>>> 41e5102c38803e61a545fd2defe14d107cc28601
>>>>>>> 4c79d4b9f607156e9777fe6895c17a1774d7332f
]
