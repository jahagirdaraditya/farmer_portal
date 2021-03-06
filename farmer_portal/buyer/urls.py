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
    path('feedback/', buyer_views.feedback , name='buyer-feedback'),
    path('track/', buyer_views.out_for_delivery , name='buyer-track'),
    path('success_stories/', buyer_views.success_stories, name='buyer-success_stories'),
    path('order-confirm/', buyer_views.order_confirm, name='buyer-order-confirm'),
]
