from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserRegistrationForm


def index(request):
	pass

def register(request):
	context = {
		'form':UserRegistrationForm(),
	}
	return render(request, 'users/register.html',context)

def create_user(request):
	for key, value in request.POST.items():
		print(key, value)
	errors = {}
	if request.POST['password2'] != request.POST['password1']:
		errors['password_mismatch'] = "Passwords do not match!"
		for key, value in errors.items():
				messages.error(request, value)
		return redirect('register')
	else:
		User.objects.create_user(request.POST['email'], 
								request.POST['username'],
								request.POST['password1'],)
		return redirect('/')

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		return redirect(request,'/')
	else:
		context = {
			'form':AuthenticationForm()
		}
		return render(request, 'users/login.html', context)

def login_user(re)