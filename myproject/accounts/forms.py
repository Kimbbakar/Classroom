from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

CHOICES=[(0,'Student'),
         (1,'Teacher')]


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    type = forms.ChoiceField(label = 'I am a ',choices=CHOICES)
    username = forms.CharField(label = 'ID (Student/Teacher) ', required=True,help_text = 'Require. only digit. length 10 (Provided with your ID card) ')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','type')


    def clean_username(self):
        data = self.cleaned_data['username']
        digit = [ '0','1','2','3','4','5','6','7','8','9' ]
        if len(data)!=10:
            raise forms.ValidationError("ID length must be 10")           
        elif data and User.objects.filter(username=data).exists():
            raise forms.ValidationError("ID must be unique.")

        else:
            for i in data:
                if i not in digit:
                    raise forms.ValidationError("ID only contain digits (0-9).")                            

        return data