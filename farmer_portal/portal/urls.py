from django.urls import path, include
from . import views as portal_views
from farmers import views as farmer_views


urlpatterns = [
    path('', portal_views.home , name='portal-home'),
    path('farmer/', include('farmers.urls')),
<<<<<<< HEAD
    path('buyer/', include('buyer.urls')),
    path('admin_portal/', include('admin_portal.urls')),
    path('service/', include('services.urls')),
=======
    path('service/', include('services.urls')),
    path('buyer/', include('buyer.urls')),
    path('admin_portal/', include('admin_portal.urls')),
    path('login/', portal_views.login, name='login')
>>>>>>> 530bf430b5b84604526cabe17fc2eed216ee45bb
]
