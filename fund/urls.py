from django.urls import path
from . import views

urlpatterns=[
    path('add_fund',views.add_fund,name="add_fund"),
    path('fund_list',views.fund_list,name="fund_list"),
    path('edit_fund/<int:pk>',views.edit_fund,name="edit_fund"),
    path('delete_fund/<int:pk>',views.delete_fund,name="delete_fund"),
    path('search_fund',views.search_fund,name="search_fund"),
]