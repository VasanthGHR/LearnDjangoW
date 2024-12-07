from django.urls import path
from . import views

urlpatterns = [    
    path('home/', views.HomePageView.as_view(), name='homepage'),
    path('', views.HomePageView.as_view(), name='homepage'),
    path('about/', views.AboutView.as_view(), name='aboutpage'),
]