from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='inspiration'),
    path('about/', views.about, name='inspiration-about'),
    path('register/', views.about, name='inspiration-register'),
]