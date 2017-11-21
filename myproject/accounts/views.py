from django.shortcuts import render
from .forms import SignUpForm

# Create your views here.

def signup(request):

    if request.method =='POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            return render(request, 'signup.html', {'form': form})            

    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})