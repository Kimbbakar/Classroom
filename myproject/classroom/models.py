from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class course(models.Model):
    course_id = models.CharField(max_length=10,  primary_key=True)
    course_name = models.CharField(max_length=30)
    faculty = models.CharField(max_length=10)
    semester = models.ForeignKey(User, related_name='faculty', default= 'Admin' )


class user_type(models.Model):
    user = models.ForeignKey(User,related_name = 'type' )
    role = models.IntegerField()

class registration(models.Model):
    user = models.ForeignKey(User,related_name = 'registration' )
    course = models.ForeignKey(course, related_name='registration')

class lecture(models.Model): 	
    course = models.ForeignKey(course, related_name='lectures', default= 'Admin' )
    name = models.CharField(max_length=20)
    link = models.CharField(max_length=30)
    description = models.CharField(max_length=400,null=True)
    date = models.DateField(default=date.today)