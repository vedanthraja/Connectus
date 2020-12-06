from django.db import models

# Create your models h

class Project(models.Model):
    pass

class student(models.Model):
    username = models.CharField(unique=True, max_length = 30)
    password = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    institiute_name = models.CharField(max_length = 100)
    projects = models.ManyToManyField(Project, null=True)

    def __str__(self):
        return self.username



