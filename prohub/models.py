from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects')
    title = models.CharField(max_length=50)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile')
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=200)

    def __str__(self):
        return self.name
