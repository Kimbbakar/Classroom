from django import forms
from django.contrib.auth.models import User
from .models import lecture,course,post
from datetime import date

class NewLectureForm(forms.ModelForm):

    name = forms.CharField(label = 'Lecture Name',max_length=20)
    description = forms.CharField(widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'Description about todays lecture.'}
        ),
        max_length=400,
        help_text='The max length of the text is 400.'
    )


    date = forms.DateField(initial=date.today(),widget=forms.SelectDateWidget() )
    link = forms.URLField(initial='http://',label='Slid Link')

    class Meta:
        model = lecture 
        fields = ['name','link','description','date' ]

SEMESTER = [('Fall','Fall'),('Summer','Summer'),('Spring','Spring')]


class NewCourseForm(forms.ModelForm):
    course_id = forms.CharField(max_length=20,help_text='Section number should be mentioned. e.g. EEE123.1')
    course_name = forms.CharField(max_length=100)    
    semester = forms.ChoiceField(choices=SEMESTER) 

    class Meta:
        model = course
        fields = ['course_id','course_name','semester']

class StudentAddForm(forms.Form):
    student_id = forms.CharField(widget=forms.Textarea(
            attrs={'rows': 5}
        ),
        max_length=400,
        help_text='ID should be valid and separated by semicolon(;).' 
    )
  

    def clean_student_id(self):
        data = self.cleaned_data['student_id'] 


        student  = list(map(str,data.strip().split(';') ))



        invalid = list()
        for i in student: 
            if len(i)!=0:
                if User.objects.filter(username=i).exists() == False :
                    invalid.append(i)

        if len(invalid)!=0: 
 
            warning = "Invalid id: "
            for i in invalid:
                warning+=(i + ';')
            raise forms.ValidationError(warning )

        return data

class PostCommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(
            attrs={'rows': 2}
        ),
        max_length=100,
        help_text='The max length of the text is 100.'
    )

    class Meta:
        model = post
        fields = ['comment']