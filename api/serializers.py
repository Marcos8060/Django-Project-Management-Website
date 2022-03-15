from prohub.models import Project,Profile,ReviewRating
from rest_framework import serializers
from django.contrib.auth.models import User


class ProjectSerilizer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Project
        fields = ['id','owner','image','title','description','pub_date','location']


class UserSerializer(serializers.ModelSerializer):
    projects = serializers.PrimaryKeyRelatedField(many=True,queryset=Project.objects.all())
    class Meta:
        model = User
        fields = ['id','username','projects']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewRating
        fields = ['subject','review','rating','ip','status','created_at','updated_at']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['project','profile_picture','name','bio']


