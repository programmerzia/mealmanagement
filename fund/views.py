from django.shortcuts import render,get_object_or_404,redirect
from fund.forms import FundForm, EditForm
from .models import Fund
from datetime import datetime
from django.contrib import messages
from django.db.models import Sum,F,Count
# Create your views here.

def fund_list(request):
    today = datetime.now()
    funds = Fund.objects.filter(fund_date__month=today.month,fund_date__year=today.year)
    context = {
        'today':today,
        'funds':funds
    }
    return render(request,'fund/fund_list.html',context)

def add_fund(request):
    message = False
    form = FundForm()
    if request.method == 'POST':
        form = FundForm(request.POST)
        if form.is_valid():
            form.save()
            message = True
            form = FundForm()
    context = {
        'form':form,
        'message':message
    }
    return render(request,'fund/add_fund.html',context)        

def search_fund(request):
    today = datetime.now()
    funds = Fund.objects.filter(fund_date__month=today.month,fund_date__year=today.year)
    if request.method=='POST':
        sdate = request.POST.get('selected_date')
        sdate = datetime.strptime(sdate,"%Y-%m-%d")
        funds = Fund.objects.filter(fund_date__month=sdate.month,fund_date__year=sdate.year)
        today = sdate
    context = {
        'today':today,
        'funds':funds
    }
    return render(request,'fund/fund_list.html',context)

def edit_fund(request,pk):
    fund = get_object_or_404(Fund,pk=pk)
    form = FundForm(instance=fund)
    if request.method == 'POST':
        form = EditForm(request.POST,instance=fund)
        if form.is_valid():
            form.save()
            messages.success(request,'Updated')
            return redirect('fund_list')
    return render(request,'fund/edit_fund.html',{'form':form})

def delete_fund(request,pk):
    fund = get_object_or_404(Fund,pk=pk)
    fund.delete()
    messages.success(request,'Deleted')
    return redirect('fund_list')
