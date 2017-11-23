from django.shortcuts import render,redirect 
from .forms import SignUpForm,LogInForm
from classroom.models import user_type 
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate 

# Create your views here.

def signup(request):

    if request.method =='POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit = False)
            user.save()
            user_type.objects.create(user = user, role = form['type'].value() )
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

 
def login(request):
    
    Warning = 0

    if request.method=='POST':
        form = LogInForm(request.POST)

        if form.is_valid():            
            user = authenticate(request, username=form['username'].value(), password=form['password'].value() )
            if user is not None:
                auth_login(request,user)
                return redirect('home')
            else:
                Warning = 1
        else: 
            Warning = 2 
    else: 
        form = LogInForm()

    return render(request,'login.html',{'form':form , 'Warning':Warning } )