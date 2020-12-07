from django.contrib import admin
from .models import Project,Comment,student,Report
# Register your models here.
admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(student)
admin.site.register(Report)