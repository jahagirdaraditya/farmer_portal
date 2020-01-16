from django.urls import path, include
from . import views as farmer_views

urlpatterns = [
    # path('', farmer_views.dashboard , name='farmer-dashboard'),
    path('dashboard/', farmer_views.dashboard , name='farmer-dashboard'),
]
