from django.shortcuts import render,redirect
from accounts.models import User
from accounts.forms import RegistrationForm, UserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
	return render(request ,'accounts/index.html')

def register(request):
	form = RegistrationForm()
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'Account has been created !')
			return redirect('login')
	return render(request,'accounts/register.html',{'form':form})	


@login_required	
def profile(request):
	user = request.user
	form = UserForm(instance=user)
	if request.method == 'POST':
		form = UserForm(request.POST,request.FILES,instance=user)
		if form.is_valid():
			form.save()
			return redirect('profile')
	return render(request,'accounts/profile.html',{'form':form})	