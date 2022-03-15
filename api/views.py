from api.permissions import IsOwnerOrReadOnly
from prohub.models import Project,ReviewRating,Profile
from api.serializers import ProjectSerilizer,UserSerializer,ReviewSerializer,ProfileSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly



class ProjectList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerilizer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    queryset = Project.objects.all()
    serializer_class = ProjectSerilizer

class UserList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReviewRatingView(generics.ListAPIView):
    queryset = ReviewRating.objects.all()
    serializer_class = ReviewSerializer


class ProfileView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer