from prohub.models import Project,Profile,ReviewRating
from rest_framework import serializers


class ProjectSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id','image','title','description','pub_date','location']

