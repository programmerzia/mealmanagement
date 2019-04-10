from django.urls import path
from . import views

urlpatterns = [
	path('add_meal', views.add_meal, name="add_meal"),
	path('meal_list', views.meal_list, name="meal_list"),
	path('search_meal', views.search_meal, name="search_meal"),
]