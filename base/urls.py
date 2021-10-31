from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-order', views.create_order, name='create_order'),
    path('my-orders', views.view_orders, name='my_orders'),
]
