from django.db import models
from accounts.models import User

# Create your models here.
class Fund(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="funds")
    amount = models.IntegerField(default=0)
    fund_date = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
