from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class course(models.Model):
    course_id = models.CharField(max_length=10,  primary_key=True)
    course_name = models.CharField(max_length=30)
    faculty = models.CharField(max_length=10)
    semester = models.CharField(max_length=10)
 


class lecture(models.Model): 	
    course = models.ForeignKey(course, related_name='lectures', default= 'Admin' )
    name = models.CharField(max_length=20)
    link = models.CharField(max_length=30)
    description = models.CharField(max_length=400,null=True)
    date = models.DateField(default=date.today)