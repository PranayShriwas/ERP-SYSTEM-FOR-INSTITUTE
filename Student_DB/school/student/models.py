from django.db import models

# Create your models here.


class AddCourses(models.Model):
    course = models.CharField(max_length=200)
    fees = models.IntegerField()
    duration = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.course


class Formdata(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=505)

    def __str__(self):
        return self.name


class Addstudent(models.Model):
    sname = models.CharField(max_length=500)
    semail = models.EmailField(max_length=254)
    smobile = models.IntegerField()
    saddress = models.CharField(max_length=1000)
    scollege = models.CharField(max_length=500)
    sdegree = models.CharField(max_length=500)
    total_amount = models.IntegerField()
    paid_amount = models.IntegerField()
    due_amount = models.FloatField()
    scourse = models.ForeignKey(AddCourses, on_delete=models.CASCADE)

    def __str__(self):
        return self.sname
