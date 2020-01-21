from django.urls import path, include
from . import views as service_views

urlpatterns = [
    # path('', farmer_views.dashboard , name='farmer-dashboard'),
    path('dashboard/', service_views.dashboard , name='service-dashboard'),
    path('profile/', service_views.profile , name='profile-check'),
    path('orders/', service_views.orders , name='service-orders'),
    path('add_location/', service_views.add_location , name='service-add_location'),
    path('save_all_addresses/', service_views.save_all_addresses , name='service-save_all_location'),
    path('statistics/', service_views.statistics , name='service-statistics'),
    # path('addProduce/', farmer_views.addProduce , name='farmer-addProduce-Form'),
    
]
