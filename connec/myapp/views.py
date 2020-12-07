
from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm, StudentRegistrationForm, CommentForm, ReportForm
# from .filters import OrderFilter
def ProjList(request):
	projs = Project.objects.all()
	context = {'projs':projs}
	return render(request,'myapp/projects/projects.html',context)

@login_required(login_url='login')
def apply(request, pk):
	proj = Project.objects.get(pk=pk)
	user = request.user
	username = user.username
	print(username)
	stud = student.objects.get(username=username)
	stud.projects.add(proj)

	return redirect('home')


@login_required(login_url='login')
def Project_details(request,pk):
	proj = Project.objects.get(pk=pk)
	lat = proj.latitude
	lon = proj.longitude
	lat1=0
	lon1=0
	if(lat[-1]=='N'):
		lat1=1
	else:
		lat1=-1
	if(lon[-1]=='E'):
		lon1=1
	else:
		lon1=-1
	l1=len(lat)
	l2=len(lat)
	lat_num = float(lat[slice(l1-2)])*lat1
	lon_num = float(lon[slice(l2-2)])*lon1
	context = {'proj':proj,'lat_num':lat_num,'lon_num':lon_num, 'id':proj.id}
	return render(request, 'myapp/project-details/detail.html',context)
@login_required(login_url='login')
def Project_comments(request,pk):
	proj = Project.objects.get(pk=pk)
	comments = Comment.objects.filter(proj=proj).order_by('-date')
	form = CommentForm()
	context = {'comments':comments, 'form':form}
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comm_txt = form.cleaned_data.get('comm_txt')
			commenter = request.user
			com = Comment.objects.create(commenter=commenter,comm_txt=comm_txt,proj=proj)
			com.save()
	return render(request,'myapp/comments.html',context)

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		form = StudentRegistrationForm()
		if request.method == 'POST':
			form = StudentRegistrationForm(request.POST)
			if form.is_valid():
				
				user1 = form.cleaned_data.get('username')
				passw = form.cleaned_data.get('password')
				mail = form.cleaned_data.get('email')
				user = User.objects.create_user(username=user1,email= mail,password=passw)
				user.save()
				form.save()
				messages.success(request, 'Account was created for ' + user1)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'myapp/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'myapp/login.html', context)

@login_required(login_url='login')
def logoutUser(request):
	logout(request)
	return redirect('login')
@login_required(login_url='login')
def myProjects(request):
	projs = Project.objects.filter(student = request.user)
	username = request.user.username	
	context = {'projs':projs,'username':username}
	return render(request,'myapp/myprojects.html',context)


@login_required(login_url='login')

def home(request):
	return render(request, 'myapp/home.html', {})


# @login_required(login_url='login')
# def home(request):
# 	orders = Order.objects.all()
# 	customers = Customer.objects.all()

# 	total_customers = customers.count()

# 	total_orders = orders.count()
# 	delivered = orders.filter(status='Delivered').count()
# 	pending = orders.filter(status='Pending').count()

# 	context = {'orders':orders, 'customers':customers,
# 	'total_orders':total_orders,'delivered':delivered,
# 	'pending':pending }

# 	return render(request, 'accounts/dashboard.html', context)

# @login_required(login_url='login')
# def products(request):
# 	products = Product.objects.all()

# 	return render(request, 'accounts/products.html', {'products':products})

# @login_required(login_url='login')
# def customer(request, pk_test):
# 	customer = Customer.objects.get(id=pk_test)

# 	orders = customer.order_set.all()
# 	order_count = orders.count()

# 	myFilter = OrderFilter(request.GET, queryset=orders)
# 	orders = myFilter.qs 

# 	context = {'customer':customer, 'orders':orders, 'order_count':order_count,
# 	'myFilter':myFilter}
# 	return render(request, 'accounts/customer.html',context)

# @login_required(login_url='login')
# def createOrder(request, pk):
# 	OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10 )
# 	customer = Customer.objects.get(id=pk)
# 	formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
# 	#form = OrderForm(initial={'customer':customer})
# 	if request.method == 'POST':
# 		#print('Printing POST:', request.POST)
# 		form = OrderForm(request.POST)
# 		formset = OrderFormSet(request.POST, instance=customer)
# 		if formset.is_valid():
# 			formset.save()
# 			return redirect('/')

# 	context = {'form':formset}
# 	return render(request, 'accounts/order_form.html', context)

# @login_required(login_url='login')
# def updateOrder(request, pk):

# 	order = Order.objects.get(id=pk)
# 	form = OrderForm(instance=order)

# 	if request.method == 'POST':
# 		form = OrderForm(request.POST, instance=order)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('/')

# 	context = {'form':form}
# 	return render(request, 'accounts/order_form.html', context)

# @login_required(login_url='login')
# def deleteOrder(request, pk):
# 	order = Order.objects.get(id=pk)
# 	if request.method == "POST":
# 		order.delete()
# 		return redirect('/')

# 	context = {'item':order}
# 	return render(request, 'accounts/delete.html', context)

