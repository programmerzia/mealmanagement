from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
	GENDER_CHOICES = (
		('male','Male'),
		('female','Female'),
		('other','Other')
	)
	contact = models.CharField(max_length=13)
	photo = models.ImageField(default='default.jpg', upload_to='user_photo')
	birthday = models.DateField(null=True,blank=True)
	join_date = models.DateField(null=True,blank=True)
	address = models.TextField(blank=True,null=True)
	gender = models.CharField(max_length=6,null=True,choices=GENDER_CHOICES,default='male')
	def __str__(self):
		return self.first_name
