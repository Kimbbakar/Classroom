"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from classroom import views
from django.contrib.auth import views as auth_views
from accounts import views as accouts_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.welcome,name='welcome' ),
    url(r'^signup/$', accouts_views.signup,name='signup' ),
    url(r'^home/$', views.home,name='home' ),
    url(r'^home/new/$', views.new_course,name='new_course' ),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^login/$', accouts_views.login, name='login'),
    url(r'^course/(?P<pk>[.\w]+)/$', views.course_view,name='course_view' ),
    url(r'^course/(?P<pk>[.\w]+)/new/$', views.new_lecture,name='new_lecture' ),
    url(r'^course/student/(?P<pk>[.\w]+)/$', views.student_view,name='student_view' ),
    url(r'^course/test/(?P<pk>[.\w]+)/$', views.test_view,name='test_view' ),
    url(r'^course/test/grade/(?P<pk>[.\w]+)/$', views.grade_view,name='grade_view' ),
    url(r'^course/test/(?P<pk>[.\w]+)/new/$', views.new_test,name='new_test' ),
    url(r'^course/student/add_student/(?P<pk>[.\w]+)/$', views.add_student,name='add_student' ),
    url(r'^course/lecture/(?P<pk>\d+)/$', views.lecture_view,name='lecture_view' ),
]
