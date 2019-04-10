from django.shortcuts import render, redirect
from .forms import AddMeal
from django.contrib import messages
from meal.models import Meal
from datetime import datetime
import calendar
from accounts.models import User
from django.db.models import Sum

# Create your views here.
today = datetime.now()

def add_meal(request):
	form = AddMeal()
	user = request.user
	if request.method == 'POST':
		form = AddMeal(request.POST)
		if form.is_valid():
			meal_date = form.cleaned_data['meal_date']
			breakfast = form.cleaned_data['breakfast']
			lunch = form.cleaned_data['lunch']
			dinner = form.cleaned_data['dinner']
			data = Meal(user=user,meal_date=meal_date,breakfast=breakfast,lunch=lunch,dinner=dinner,total=breakfast+lunch+dinner)
			data.save()
			messages.success(request,'Your meal has been added !')
	return render(request,'meal/add_meal.html',{'form':form})


def meal_list(request):
	total = Meal.objects.filter(meal_date__month=today.month,meal_date__year=today.year).aggregate(total=Sum('total'))
	users = User.objects.distinct().filter(meals__meal_date__year=today.year,meals__meal_date__month=today.month).order_by('meals__meal_date')
	daterange = calendar.monthrange(today.year,today.month)[1]
	context = {
		'users':users,
		'range':range(daterange),
		'total':total,
		'today':today
	}
	return render(request,'meal/meal_list.html',context)


def search_meal(request):
	today = datetime.now()
	total = Meal.objects.filter(meal_date__month=today.month,meal_date__year=today.year).aggregate(total=Sum('total'))
	users = User.objects.distinct().filter(meals__meal_date__year=today.year,meals__meal_date__month=today.month).order_by('meals__meal_date')
	daterange = calendar.monthrange(today.year,today.month)[1]
	if request.method == 'POST':
		sdate = request.POST.get('selected_date')
		sdate = datetime.strptime(sdate,"%m/%d/%Y")
		daterange = calendar.monthrange(sdate.year,sdate.month)[1]
		total = Meal.objects.filter(meal_date__month=sdate.month,meal_date__year=sdate.year).aggregate(total=Sum('total'))
		users = User.objects.distinct().filter(meals__meal_date__year=sdate.year,meals__meal_date__month=sdate.month).order_by('meals__meal_date')
		today = sdate
	context = {
		'users':users,
		'range':range(daterange),
		'total':total,
		'today':today
	}	
	return render(request,'meal/meal_list.html',context)
