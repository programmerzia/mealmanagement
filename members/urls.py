from django.urls import path
from . import views

urlpatterns = [
	path('add_member',views.add_member, name="add_member"),
	path('member_list',views.member_list, name="member_list"),
	path('edit_member/<int:pk>',views.edit_member, name="edit_member"),
	path('delete_member/<int:pk>',views.delete_member, name="delete_member"),
] 