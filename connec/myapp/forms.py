from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import student, Comment, Report



# from .models import Order


# class OrderForm(ModelForm):
# 	class Meta:
# 		model = Order
# 		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class StudentRegistrationForm(ModelForm):
	class Meta:
		model = student
		fields = ['username', 'email', 'password', 'institiute_name']
		widgets = {'password' : forms.PasswordInput()}

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['comm_txt']

class ReportForm(forms.ModelForm):
	class Meta:
		model = Report
		fields = ['file']
