from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import lecture

# Create your views here.

def home(request):
    lectures = lecture.objects.all()

    return render(request,'home.html',{'lectures':lectures } ) 

def lecture_view(request,pk):
    pk_lecture = lecture.objects.get(pk=pk )
    print (pk_lecture.link)
    return render(request,'lecture_view.html',{'pk_lecture':pk_lecture } ) 