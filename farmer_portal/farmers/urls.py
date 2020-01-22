from django.urls import path, include
from . import views as farmer_views

urlpatterns = [
    # path('', farmer_views.dashboard , name='farmer-dashboard'),
    path('dashboard/', farmer_views.dashboard , name='farmer-dashboard'),
    path('addProduce/', farmer_views.addProduce , name='farmer-addProduce-Form'),
    path('fpo_list/', farmer_views.fpo_list , name='fpo-list'),
    path('orders/', farmer_views.orders , name='farmer-orders'),
    path('history/', farmer_views.history , name='farmer-history'),
    path('check/', farmer_views.check , name='farmer-check'),
    path('myapplications/', farmer_views.farmerApplications, name='farmer-applications'),
    path('services/', farmer_views.services, name='farmer-services'),
    path('complaints/', farmer_views.complaint, name='farmer-complaints'),
    path('success_stories/', farmer_views.success_stories, name='farmer-success_stories')
]