from accounts.models import User
from django import forms

class MemberForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name','last_name','contact','username','password','join_date']
		widgets = {
			'join_date':forms.DateInput(attrs={'class':'datepicker'}),
		}
class MemberUpdate(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name','last_name','contact','join_date','address']
		widgets = {
			'join_date':forms.DateInput(attrs={'class':'datepicker'}),
		}
