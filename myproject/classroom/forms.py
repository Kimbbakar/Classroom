from django import forms

from .models import lecture
from datetime import date

BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
class NewLectureForm(forms.ModelForm):

    name = forms.CharField(label = 'Lecture Name',max_length=20)
    description = forms.CharField(widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'Description about todays lecture.'}
        ),
        max_length=400,
        help_text='The max length of the text is 400.'
    )


    date = date = forms.DateField(initial=date.today(),widget=forms.SelectDateWidget() )
    link = forms.CharField(
        label = 'Slid link', 
        widget=forms.Textarea(
            attrs={'rows': 1, 'placeholder': 'e.g. www.slideshare.com/abc'}
        ),
        max_length=30

    )

    class Meta:
        model = lecture 
        fields = ['name','link','description','date' ]
