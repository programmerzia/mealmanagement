from django import forms
from meal.models import Meal

class AddMeal(forms.ModelForm):
	class Meta:
		model = Meal
		fields = ['meal_date','breakfast','lunch','dinner']
		widgets = {
			'meal_date':forms.TextInput(attrs={'class':'datepicker','required':True}),
		}