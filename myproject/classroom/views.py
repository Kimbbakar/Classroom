from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import lecture,course
from datetime import date

# Create your views here.

def home(request):
    courses = course.objects.all()

    return render(request,'home.html',{'courses':courses } ) 

def course_view(request,pk):
    pk_course = course.objects.get(pk=pk )
 
    return render(request,'course_view.html',{'pk_course':pk_course } ) 


def lecture_view(request,pk):
    pk_lecture = lecture.objects.get(pk=pk )

    print (pk_lecture.course_id.course_id)
 
    return render(request,'lecture_view.html',{'pk_lecture':pk_lecture } ) 

def new_lecture(request,pk):

    courseS = course.objects.get(pk = pk)

    if request.method == 'POST':
        lecture_name = request.POST['lecture_name']
        link =request.POST['link']
        lecture_description =request.POST['lecture_description']
        lecture_date =request.POST['date']

        if (lecture_name.count(' ')==len(lecture_name) or len(lecture_name)>10  ) :
            return render(request, 'new_lecture.html',{'pk_course':courseS, 'lecture_name':lecture_name, 'lecture_description':lecture_description,'link':link,'today':lecture_date } ) 
        else: 

            lec = lecture.objects.create(
                course_id = courseS,
                name = lecture_name, 
                link = link,
                description = lecture_description,
                date = lecture_date

                )
            
            return redirect('lecture_view',pk = lec.pk )
 
    return render(request, 'new_lecture.html',{'pk_course':courseS,'lecture_name':"", 'lecture_description':"",'link':"",'today':str(date.today()) } )     
