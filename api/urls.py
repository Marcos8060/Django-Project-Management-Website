from django.urls import path
from . import views
from rest_framework import routers



urlpatterns = [
    path('projects/',views.ProjectList.as_view()),
    path('projects/<int:pk>',views.ProjectDetail.as_view()),
    path('users/',views.UserList.as_view()),
    path('users/<int:id>',views.UserDetail.as_view()),
    path('projects/<int:id>/reviews/',views.ReviewRatingView.as_view()),
    path('profile/<int:id>',views.ProfileView.as_view()),
]