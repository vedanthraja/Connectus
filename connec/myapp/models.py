from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 150)
    category = models.CharField(max_length = 150)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    collector = models.ForeignKey(User, on_delete = models.CASCADE, related_name ='collector')
    student = models.ForeignKey(User, on_delete = models.CASCADE, related_name='student')
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    cover_img = models.ImageField(upload_to = "gallery")

    def __str__(self):
        return self.title

class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete = models.CASCADE)
    comm_txt = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    proj = models.ForeignKey(Project, on_delete = models.CASCADE)

    def __str__(self):
        return self.comm_txt


class student(models.Model):
    username = models.CharField(unique=True, max_length = 30)
    password = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    institiute_name = models.CharField(max_length = 100)
    projects = models.ManyToManyField(Project, null=True)

    def __str__(self):
        return self.username



