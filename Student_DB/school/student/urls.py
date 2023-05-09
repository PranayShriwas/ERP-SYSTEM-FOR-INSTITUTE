from . import views
from django.urls import path
urlpatterns = [
    path('index/', views.index, name='index'),
    path('courses/', views.courses, name='courses'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.signup, name='signup'),
    path('viewstudents/', views.viewstudents, name='viewstudents')

]
