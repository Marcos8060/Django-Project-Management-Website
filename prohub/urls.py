from django.urls import path
from . import views


urlpatterns = [
    path('',views.home_page,name='home'),
    path('profile/',views.profile,name='profile'),
    path('register/',views.register,name='register')
]