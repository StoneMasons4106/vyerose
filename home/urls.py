from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('privacypolicy/', views.privacy_policy, name='privacypolicy')
]