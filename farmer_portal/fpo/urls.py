from django.urls import path, include
from . import views as fpo_views

urlpatterns = [
    # path('', fpo_views.dashboard , name='fpo-dashboard'),
    path('dashboard/', fpo_views.dashboard , name='fpo-dashboard'),
    path('addProduce/', fpo_views.addProduce , name='fpo-addProduce-Form'),
    path('orders/', fpo_views.orders , name='fpo-orders'),
    path('check/', fpo_views.check , name='fpo-check'),
    path('myapplications/', fpo_views.fpoApplications, name='fpo-applications'),
    path('services/', fpo_views.services, name='fpo-services'),
    path('complaints/', fpo_views.complaint, name='fpo-complaints'),
    path('success_stories/', fpo_views.success_stories, name='fpo-success_stories')
]