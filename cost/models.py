from django.db import models
from accounts.models import User

# Create your models here.
class Cost(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	amount = models.FloatField(default=0.00)
	cost_date = models.DateField(null=True,blank=True)
	comment = models.CharField(max_length=200,blank=True,null=True)

	def __str__(self):
		return str(self.cost_date)