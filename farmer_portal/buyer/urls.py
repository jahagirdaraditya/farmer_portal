from django.urls import path, include
from . import views as buyer_views

urlpatterns = [
    # path('', farmer_views.dashboard , name='farmer-dashboard'),
    path('dashboard/', buyer_views.dashboard , name='buyer-dashboard'),
    path('buy_now/', buyer_views.buy_now , name='buy_now_buyer'),
    path('checkout/', buyer_views.checkout , name='checkout_buyer'),
    path('my_orders/', buyer_views.my_order , name='buyer-my-orders'),
    path('complaint/', buyer_views.complaint , name='buyer-complaint'),
    path('profile/', buyer_views.profile , name='buyer-profile'),
]

