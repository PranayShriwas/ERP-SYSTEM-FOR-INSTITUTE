from . import views
from django.urls import path
urlpatterns = [
    path('', views.sign_up),
    path('index/', views.index),
    path('registration/', views.Form_data, name='Form_data'),
    path('loginform/', views.loginform, name='login_form'),
    path('dashboard/', views.student),
    path('courses/', views.coureses),
    path('addcoures/', views.addcoures),
    path('view_student/', views.view_student),
    path('addstudent/', views.addstudent),
    path('deletecourse/<int:uid>/', views.deletecourse, name='stucou'),
    path('deletestu/<int:uid>/', views.deletestu, name='studel'),
    path('search/', views.search),
    path('supdate/<int:uid>/', views.supdate),
    path('studentupdate/', views.studentupdate),
    
]
