from django.urls import path
from . import views

urlpatterns = [
	path('add_cost',views.add_cost, name="add_cost"),
	path('cost_list',views.cost_list, name="cost_list"),
	path('delete_cost/<int:pk>',views.delete_cost, name="delete_cost"),
	path('search_cost',views.search_cost, name="search_cost"),
]