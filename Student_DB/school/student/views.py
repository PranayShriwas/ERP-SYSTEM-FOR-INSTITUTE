from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages


def student(request):
    return render(request, 'dashboard.html')


def coureses(request):
    co = AddCourses.objects.all()
    return render(request, 'courses.html', {'co': co})


def view_student(request):
    return render(request, 'viewstudents.html')


def index(request):
    return render(request, 'index.html')


def sign_up(request):
    return render(request, 'sign-up.html')


def Form_data(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        if Formdata.objects.filter(email=email).exists():
            messages.error(request, 'Email is already exists')
            return redirect('/signup/')
        else:
            Formdata.objects.create(name=name, email=email, password=password)
            messages.SUCCESS(request, 'Registration Successfully')
            return redirect('/')


def loginform(request):
    if request.method == "POST":
        email = request.POST['Email']
        User_password = request.POST['Password']
        if student.objects.filter(email=email).exists():
            obj = student.objects.get(email=email)
            password = obj.password
            if check_password(User_password, password):
                return redirect('/dashboard/')
            else:
                messages.error(request, 'Password incorrect')
                return redirect('/')
        else:
            messages.error(request, 'Email is not registered')
            return redirect('/index/')


def addcoures(request):
    if request.method == 'POST':
        c_name = request.POST['Coursename']
        c_fees = request.POST['Coursefees']
        c_duration = request.POST['Duration']
        c_desc = request.POST['CourseDesc']
        messages.success(request, 'Course added suceessfully')
        AddCourses.objects.create(
            course=c_name, fees=c_fees, duration=c_duration, desc=c_desc
        )
        return redirect('/courses/')


def addstudent(request):
    if request.method == 'POST':
        stu_name = request.POST.get('Name')
        stu_email = request.POST.get('Email')
        stu_mobile = request.POST.get('Mobile')
        stu_college = request.POST.get('College')
        stu_degree = request.POST.get('Degree')
        stu_address = request.POST.get('Address')
        stu_addcourse_id = request.POST.get('Course')
        total_amount = request.POST.get('qty')
        paid_amount = request.POST.get('cost')
        due_amount = request.POST.get('DueAmount')
        stu_course = AddCourses.objects.get(id=stu_addcourse_id)
        if Addstudent.objects.filter(semail=stu_email).exists():
            messages.error(request, 'Email is alreay exists')
            return redirect('addstudent')
        elif Addstudent.objects.filter(smobile=stu_mobile).exists():
            messages.error(request, 'Mobile Number Is Already Exists')
            return redirect('addstudent')
        else:
            Addstudent.objects.create(sname=stu_name,
                                      semail=stu_email,
                                      smobile=stu_mobile,
                                      sdegree=stu_degree,
                                      saddress=stu_address,
                                      scourse=stu_course,
                                      total_amount=total_amount,
                                      paid_amount=paid_amount,
                                      due_amount=due_amount)
            messages.success(request, 'Student Added SuccessFully!!')
            stu = Addstudent.objects.all()
            addcoures = AddCourses.objects.all()
            return redirect(request, '/viewstudent/', {'stu': stu, 'addcoures': addcoures, })
    else:
        stu = Addstudent.objects.all()

        addcoures = AddCourses.objects.all()
        return render(request, '/viewstudent/', {'stu': stu, 'addcoures': addcoures})
