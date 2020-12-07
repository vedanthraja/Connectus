from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
	path('',views.ProjList, name = "index"),
	path('<int:pk>/',views.Project_details, name='details'),
	path('<int:pk>/comments/',views.Project_comments,name='comments'),
	path('myprojects/',views.myProjects, name='myprojects')
]

#test