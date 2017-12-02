from django.db import models
from django.contrib.auth.models import User
from datetime import date
from datetime import datetime 

# Create your models here.

class course(models.Model):
    course_id = models.CharField(max_length=10,  primary_key=True)
    course_name = models.CharField(max_length=30)
    faculty = models.ForeignKey(User, related_name='courses', default= 'Admin' )
    semester = models.CharField(max_length=10)


class user_type(models.Model):
    user =models.OneToOneField(User,related_name = 'type',on_delete=models.CASCADE,primary_key=True)
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

class post(models.Model):
    user = models.ForeignKey(User,related_name = 'posts' )
    lecture = models.ForeignKey(lecture,related_name = 'posts' )
    comment = models.CharField(max_length=100)
    date = models.DateField(default=date.today)  
