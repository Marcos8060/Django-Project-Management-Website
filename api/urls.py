from django.urls import path
from . import views


urlpatterns = [
    path('projects/',views.ProjectList.as_view()),
    path('projects/<int:pk>',views.ProjectDetail.as_view()),
    path('users/',views.UserList.as_view()),
    path('users/<int:id>',views.UserDetail.as_view()),
]