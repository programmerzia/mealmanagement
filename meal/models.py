from django.db import models
from accounts.models import User
# Create your models here.
class Meal(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="meals")
	meal_date = models.DateField(null=True,blank=True)
	breakfast = models.FloatField(default=0.0)
	lunch = models.SmallIntegerField(default=0)
	dinner = models.SmallIntegerField(default=0)
	total = models.FloatField(default=0.0)

	def __str__(self):
		return str(self.user.username)