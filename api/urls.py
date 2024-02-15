"""
URL configuration for cfehome project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api import urls as apiURLS
from . import views

urlpatterns = [
    path('', views.apiHome),
    # path('<int:id>/', views.studentDetails),
    path('<int:id>/', views.StudentDetailAPIView.as_view()),
    path('create/', views.StudentCreateAPIView.as_view()),
    path('list/', views.StudentListAPIView.as_view()),
    path('list-create/', views.StudentListCreateAPIView.as_view()),  
    path('books/', views.bookList),
    path('all-in-one-for-student/', views.allInOneForStudent),
    path('all-in-one-for-student/<int:id>/', views.allInOneForStudent),
    path('student/<int:id>/update/', views.UpdateStudentAPIView.as_view()),
    path('student/<int:id>/delete/', views.DeleteStudentAPIView.as_view()),
    path('student/all-in-one-using-mixins/', views.AllInOneForStudentWithMixin.as_view()),
    path('student/all-in-one-using-mixins/create/', views.AllInOneForStudentWithMixin.as_view()),
    path('student/all-in-one-using-mixins/detail/<int:id>/', views.AllInOneForStudentWithMixin.as_view()),
    path('student/all-in-one-using-mixins/update/<int:id>/', views.AllInOneForStudentWithMixin.as_view()),
    path('student/all-in-one-using-mixins/destroy/<int:id>/', views.AllInOneForStudentWithMixin.as_view()),
    path('some-random/', views.SomeRandom.as_view()),
    path('some-random/<int:id>/detail/', views.SomeRandom.as_view()),
    path('some-random/<int:id>/delete/', views.SomeRandom.as_view()),
    path('some-random/create/', views.SomeRandom.as_view()),
    path('some-random/<int:id>/update/', views.SomeRandom.as_view()),
]
