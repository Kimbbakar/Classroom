from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class lecture(models.Model):
#   course_id =  TODO

    name = models.CharField(max_length=30, unique=True)
    lecture_no =  models.IntegerField ()
    link = models.CharField(max_length=20)
    description = models.CharField(max_length=400,null=True)
    date = models.DateField(default=date.today)