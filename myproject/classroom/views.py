from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import lecture,course,registration,post
from datetime import date
from .forms import NewLectureForm,NewCourseForm,StudentAddForm,PostCommentForm
from django.contrib.auth.decorators import login_required


def isok(request,role):
    return request.user.type.role==role

 
def welcome(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    return render(request,'welcome.html')

@login_required(login_url='/')
def home(request):
    user = request.user
    courses = user.registration.all()
    return render(request,'home.html',{'courses':courses } ) 

@login_required(login_url='/')
def course_view(request,pk):
    pk_course =get_object_or_404(course,pk=pk )
 
    return render(request,'course_view.html',{'pk_course':pk_course } ) 

@login_required(login_url='/')
def lecture_view(request,pk):
    pk_lecture = lecture.objects.get(pk=pk ) 
    posts = pk_lecture.posts.all()
 

    if request.method == 'POST':
        form = PostCommentForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.lecture = pk_lecture

            post.save()
            form = PostCommentForm()

    else: 
        form = PostCommentForm()
 
    return render(request,'lecture_view.html',{'pk_lecture':pk_lecture ,'form':form,'posts':posts } ) 

@login_required(login_url='/')
def new_lecture(request,pk):

    if isok(request,0):
        return redirect('home')

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

@login_required(login_url='/')
def new_course(request):

    if isok(request,0):
        return redirect('home')


    if request.method == 'POST':

        form = NewCourseForm(request.POST)

        if form.is_valid():
            sub = form.save(commit=False) 
            sub.faculty = request.user
            sub.semester = sub.semester + ' ' + str(date.today().year)
            sub.save() 
            registration.objects.create(user=request.user,course = sub)
            return redirect('course_view',pk = sub.pk )
    else: 
        form = NewCourseForm()
    return render(request, 'new_course.html',{'form':form } )   

@login_required(login_url='/')
def student_view(request,pk):
    if isok(request,0):
        return redirect('home')

    pk_course = course.objects.get(pk=pk ) 
 
    return render(request,'student_view.html',{'pk_course':pk_course } ) 

@login_required(login_url='/')
def add_student(request,pk):

    if isok(request,0):
        return redirect('home')
 
    pk_course = course.objects.get(pk=pk )  
    students = pk_course.registration.all()
    if request.method == 'POST':
        form = StudentAddForm(request.POST)

        if form.is_valid(): 

            student = (form['student_id'].value())
            student = map(str,student.strip().split(';') )

            for i in student:
                if len(i)==0:
                    continue

                tmp_user = User.objects.get(username=i)

                if students.filter(user =tmp_user).exists() == False :
                    registration.objects.create(course=pk_course,user = tmp_user  ) 
            return redirect('student_view',pk=pk_course.pk )
    else: 
        form = StudentAddForm()
    return render(request, 'add_student.html',{'pk_course':pk_course, 'form':form } )  
