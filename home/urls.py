from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('dashboard', views.open_dashboard, name='dashboard'),
    path('credits', views.credits_page, name='credits-page'),
]
