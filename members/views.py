from django.shortcuts import render,redirect
from accounts.models import User
from members.forms import MemberForm,MemberUpdate
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.
def member_list(request):
	member_list = User.objects.all()
	paginator = Paginator(member_list,10)
	page = request.GET.get('page')
	members = paginator.get_page(page)
	return render(request,'members/member_list.html',{'members':members})
def add_member(request):
	form = MemberForm()
	if request.method=='POST':
		form = MemberForm(request.POST)
		if form.is_valid():
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			contact = form.cleaned_data['contact']
			join_date = form.cleaned_data['join_date']
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user,created = User.objects.get_or_create(username=username,password=password,first_name=first_name,last_name=last_name,contact=contact,join_date=join_date)
			if created:
				user.set_password(password)
				user.save()
				messages.success(request,'Member has been added !')
				return redirect('add_member')
	return render(request,'members/add_member.html',{'form':form})	
def edit_member(request,pk):
	member = User.objects.get(pk=pk)
	form = MemberUpdate(instance=member)
	if request.method=='POST':
		form = MemberUpdate(request.POST,instance=member)
		if form.is_valid():
			form.save()
			messages.success(request,'Member has been updated !')
			return redirect('member_list')
	return render(request,'members/edit_member.html',{'form':form})	
def delete_member(request,pk):
	member = User.objects.get(pk=pk)
	member.delete()
	messages.success(request,'Member has been deleted !')
	return redirect('member_list')					