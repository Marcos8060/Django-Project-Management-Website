from django.db import models

# Create your models here.
class Project(models.Model):
    image = models.ImageField(upload_to='projects')
    title = models.CharField(max_length=50)
    description = models.TextField()
    pub_date = models.DateTimeField()
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.title
