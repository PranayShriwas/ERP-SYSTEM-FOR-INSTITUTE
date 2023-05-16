from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
from django.contrib import messages


def student(request):
    return render(request, 'dashboard.html')


def coureses(request):
    co = AddCourses.objects.all()
    return render(request, 'courses.html', {'co': co})


def view_student(request):
    stu = Addstudent.objects.all()
    addcoures = AddCourses.objects.all()
    return render(request, 'viewstudents.html', {'stu': stu, 'addcoures': addcoures})


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
        stu_name = request.POST.get('sname')
        stu_email = request.POST.get('semail')
        stu_mobile = request.POST.get('smobile')
        stu_college = request.POST.get('scollege')
        stu_degree = request.POST.get('sdegree')
        stu_address = request.POST.get('saddress')
        stu_addcourse_id = request.POST.get('course')
        total_amount = request.POST.get('total_amount')
        paid_amount = request.POST.get('paid_amount')
        due_amount = request.POST.get('due_amount')
        stu_course = AddCourses.objects.get(id=stu_addcourse_id)
        Addstudent.objects.create(sname=stu_name,
                                  semail=stu_email,
                                  smobile=stu_mobile,
                                  scollege=stu_college,
                                  sdegree=stu_degree,
                                  saddress=stu_address,
                                  scourse=stu_course,
                                  total_amount=total_amount,
                                  paid_amount=paid_amount,
                                  due_amount=due_amount)
        messages.success(request, 'Student Added SuccessFully!!')
        return redirect("/view_student/")

    #     if Addstudent.objects.filter(semail=stu_email).exists():
    #         messages.error(request, 'Email is alreay exists')
    #         return redirect('/view_student/')
    #     elif Addstudent.objects.filter(smobile=stu_mobile).exists():
    #         messages.error(request, 'Mobile Number Is Already Exists')
    #         return redirect('/view_student/')
    #     else:
    #         Addstudent.objects.create(sname=stu_name,
    #                                   semail=stu_email,
    #                                   smobile=stu_mobile,
    #                                   scollege=stu_college,
    #                                   sdegree=stu_degree,
    #                                   saddress=stu_address,
    #                                   scourse=stu_course,
    #                                   total_amount=total_amount,
    #                                   paid_amount=paid_amount,
    #                                   due_amount=due_amount)
    #         messages.success(request, 'Student Added SuccessFully!!')
    #         stu = Addstudent.objects.all()
    #         addcoures = AddCourses.objects.all()
    #         return redirect("/view_student/")
    # else:
    #     stu = Addstudent.objects.all()

    #     addcoures = AddCourses.objects.all()
    #     return redirect("/view_student/")


def deletecourse(request, uid):
    AddCourses.objects.filter(id=uid).delete()
    return redirect('/courses/')


def deletestu(request, uid):
    Addstudent.objects.filter(id=uid).delete()
    return redirect('/view_student/')

# For Search student


def search(request):
    if 'q' in request.GET['q']:
        q = request.GET['q']
        multiple_q = Q(Q(sname_icontains=q) | Q(
            semail_icontains=q)) | Q(smobile_icontains=q)
        stu = Addstudent.objects.filter(multiple_q)
    else:
        stu = Addstudent.objects.all()
    context = {
        'stu': stu
    }
    return render(request, 'viewstudents.html/', context)

def supdate(request,uid):
    cou = AddCourses.objects.all()
    return render(request,'update.html',{'uid':uid,'course':cou})

def studentupdate(request):
    if request.method=="POST":
        uid = request.POST['hide']
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        course = request.POST['course']
        course = AddCourses.objects.get(id=course)
        Addstudent.objects.filter(id=uid).update(sname=name,semail=email,smobile=mobile,
                                                 scourse=course)
        return redirect('/view_student/')
