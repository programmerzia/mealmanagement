from django.shortcuts import render,redirect
from .models import Cost
from .forms import CostForm
from django.contrib import messages
from django.core.paginator import Paginator
from datetime import datetime
from django.db.models import Sum
# Create your views here.
today = datetime.now()
def cost_list(request):
	total_list = Cost.objects.filter(cost_date__month=today.month,cost_date__year=today.year).order_by('-cost_date')
	total_cost = Cost.objects.filter(cost_date__month=today.month,cost_date__year=today.year).aggregate(amount=Sum('amount'))
	paginator = Paginator(total_list,31)
	page = request.GET.get('page')
	costs = paginator.get_page(page)
	return render(request,'cost/cost_list.html',{'costs':costs,'today':today,'total':total_cost})
def search_cost(request):
	today = datetime.now()
	total_cost = Cost.objects.filter(cost_date__month=today.month,cost_date__year=today.year).aggregate(amount=Sum('amount'))
	total_list = Cost.objects.filter(cost_date__month=today.month,cost_date__year=today.year)
	if request.method == 'POST':
		selected_date = request.POST.get('selected_date')
		sdate = datetime.strptime(selected_date,'%m/%d/%Y')
		total_cost = Cost.objects.filter(cost_date__month=sdate.month,cost_date__year=sdate.year).aggregate(amount=Sum('amount'))
		total_list = Cost.objects.filter(cost_date__month=sdate.month,cost_date__year=sdate.year)
		today = sdate
	paginator = Paginator(total_list,31)
	page = request.GET.get('page')
	costs = paginator.get_page(page)
	return render(request,'cost/cost_list.html',{'costs':costs,'today':today,'total':total_cost})
def add_cost(request):
	form = CostForm()
	if request.method=='POST':
		form = CostForm(request.POST)
		if form.is_valid():
			user = request.user
			cost_date = form.cleaned_data['cost_date']
			amount = form.cleaned_data['amount']
			comment = form.cleaned_data['comment']
			data = Cost(user=user,cost_date=cost_date,amount=amount,comment=comment)
			data.save()
			messages.success(request,'Cost has been added !')
			return redirect('cost_list')
	return render(request,'cost/add_cost.html',{'form':form})

def delete_cost(request,pk):
	cost = Cost.objects.get_object_or_404(pk=pk)
	cost.delete()
	messages.success(request,'Cost has been added !')
	return redirect('cost_list')