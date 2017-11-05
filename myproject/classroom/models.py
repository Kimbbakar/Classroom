from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class lecture(models.Model):
#	course_id =  TODO
	lecture_id =  models.AutoField(primary_key=True)
	slid_link = models.CharField(max_length=20)
	description = models.CharField(max_length=400,null=True)
