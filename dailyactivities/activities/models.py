from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Activity_model(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	Date = models.DateTimeField(auto_now_add=True)
	Activity_name = models.CharField(max_length=50,blank=False,null=False)
	Activity = models.CharField(max_length=1000,blank=False,null=False)
	file = models.FileField(upload_to='uploads/')

	class Meta():
		db_table='activity_model'
