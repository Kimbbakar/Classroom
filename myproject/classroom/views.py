from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import lecture
from datetime import date

# Create your views here.

def home(request):
    lectures = lecture.objects.all()

    return render(request,'home.html',{'lectures':lectures } ) 

def lecture_view(request,pk):
    pk_lecture = lecture.objects.get(pk=pk )
 
    return render(request,'lecture_view.html',{'pk_lecture':pk_lecture } ) 

def new_lecture(request):

    if request.method == 'POST':
        lecture_name = request.POST['lecture_name']
        lecture_no =request.POST['lecture_no']
        link =request.POST['link']
        lecture_description =request.POST['lecture_description']
        lecture_date =request.POST['date']

        if (lecture_name.count(' ')==len(lecture_name) or len(lecture_name)>10 or (lecture_no is None) or  link.count(' ')>0 or len(link)>20) :
            return render(request, 'new_lecture.html',{'lecture_name':lecture_name, 'lecture_description':lecture_description,'link':link,'lecture_no':lecture_no,'today':lecture_date } ) 
        else:
            return render(request, 'new_lecture.html',{'lecture_name':"", 'lecture_description':"",'link':"",'lecture_no':"",'today': str(date.today()) } )     
            
    print (date.today() )
 
    return render(request, 'new_lecture.html',{'lecture_name':"", 'lecture_description':"",'link':"",'lecture_no':"",'today':str(date.today()) } )     
