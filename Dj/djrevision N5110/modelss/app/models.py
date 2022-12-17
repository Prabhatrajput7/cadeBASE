from pyexpat import model
from django.db import models

# Create your models here.

class Sports(models.Model):
    gname = models.CharField(max_length=20)

    def __str__(self):
        return self.gname

class Subject(models.Model):
    sname = models.CharField(max_length=20)

    def __str__(self):
        return self.sname

class Teacher(models.Model):
    tname = models.CharField(max_length=20)
    sname = models.ForeignKey('Student',on_delete=models.CASCADE)
    sjname = models.ForeignKey('Subject',on_delete=models.CASCADE)

    def __str__(self):
        return self.tname

class Student(models.Model):
    name = models.CharField(max_length=20)
    rollno = models.IntegerField()
    subject = models.ManyToManyField(Subject, through='Teacher')
    # class_teacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True,blank=True)
    game = models.ForeignKey(Sports,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("name", "rollno")        

"""

class Student(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=30)
    students = models.ManyToManyField(Student, through='Enrollment')

    def __str__(self):
        return self.name        

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField()
    final_grade = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        unique_together = [['student', 'course']]
"""