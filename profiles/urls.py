from django.urls import path
from . import views

urlpatterns = [
    path('me', views.profile, name='me'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('change_password', views.change_password, name='change_password'),
]