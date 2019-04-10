from django import forms
from cost.models import Cost

class CostForm(forms.Form):
	cost_date = forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'class':'datepicker'
                                }),required=True)
	amount = forms.FloatField(required=True)
	comment = forms.CharField(required=True)
