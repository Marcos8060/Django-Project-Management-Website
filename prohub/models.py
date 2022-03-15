from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Project(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects')
    title = models.CharField(max_length=50)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('details',args=[self.id])


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile')
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ReviewRating(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=100,blank=True)
    review = models.TextField(max_length=250,blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20,blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject



