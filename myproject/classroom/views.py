from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import lecture,course
from datetime import date
from .forms import NewLectureForm,NewCourseForm
 
def home(request):
    user = request.user
    courses = user.courses.all() 
    return render(request,'home.html',{'courses':courses } ) 

def course_view(request,pk):
    pk_course = course.objects.get(pk=pk )
 
    return render(request,'course_view.html',{'pk_course':pk_course } ) 


def lecture_view(request,pk):
    pk_lecture = lecture.objects.get(pk=pk ) 
 
    return render(request,'lecture_view.html',{'pk_lecture':pk_lecture } ) 

def new_lecture(request,pk):

    courseS = course.objects.get(pk = pk)

    if request.method == 'POST':

        form = NewLectureForm(request.POST)

        if form.is_valid():
            lec = form.save(commit=False) 
            lec.course = courseS
            lec.save() 
            return redirect('lecture_view',pk = lec.pk )
        else: 
            return render(request, 'new_lecture.html',{'pk_course':courseS,'form':form } ) 
    return render(request, 'new_lecture.html',{'pk_course':courseS,'form':NewLectureForm() } )     


def new_course(request):

    if request.method == 'POST':

        form = NewCourseForm(request.POST)

        if form.is_valid():
            sub = form.save(commit=False) 
            sub.faculty = request.user
            sub.semester = sub.semester + ' ' + str(date.today().year)
            sub.save() 
            return redirect('course_view',pk = sub.pk )
    else: 
        form = NewCourseForm()
    return render(request, 'new_course.html',{'form':form } )   