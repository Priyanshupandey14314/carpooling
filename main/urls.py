# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('contact/',views.contact_us,name='contact'),
    path('offer_ride/', views.offer_ride, name='offer_ride'),
    path('find_ride/', views.find_ride, name='find_ride'),
    path('user_login/',views.user_login,name="user_Login")
]
