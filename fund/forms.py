from django import forms
from .models import Fund

class FundForm(forms.ModelForm):

    class Meta:
        model = Fund
        fields = ['user','amount','fund_date']
        widgets = {
			'fund_date':forms.DateInput(attrs={'class':'datepicker','required':True}),
		}

class EditForm(forms.ModelForm):

    class Meta:
        model = Fund
        fields =['user','fund_date','amount']
        widgets = {
			'fund_date':forms.DateInput(attrs={'class':'datepicker','required':True}),
		}
