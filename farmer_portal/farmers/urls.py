from django.urls import path, include
from . import views as farmer_views

urlpatterns = [
    # path('', farmer_views.dashboard , name='farmer-dashboard'),
    path('dashboard/', farmer_views.dashboard , name='farmer-dashboard'),
    path('addProduce/', farmer_views.addProduce , name='farmer-addProduce-Form'),
    path('check/', farmer_views.check , name='farmer-check'),
    path('myapplications/', farmer_views.farmerApplications, name='farmer-applications'),
<<<<<<< HEAD
    path('services/', farmer_views.services, name='farmer-services'),
    path('complaints/', farmer_views.complaint, name='farmer-complaints')
]
=======
]
>>>>>>> 6b637f2839f8bed860549d1ea7cb25e4c278424f
