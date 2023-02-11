from django.db import models

# Create your models here.
from turtle import title
from django.db import models
from django.contrib.auth.models import User

STATUS=((0, 'Draft'),(1, 'Published'))
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(max_length=200, unique=True)
    author=models.ForeignKey(to=User, on_delete=models.CASCADE) ##if user is deleted the content will also be deleted
    status=models.IntegerField(choices=STATUS, default=0) ## Differenciates between draft content and completed content

    def __str__(self):
        return self.title