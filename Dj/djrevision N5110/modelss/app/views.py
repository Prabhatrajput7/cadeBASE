from django.shortcuts import render
from matplotlib.style import context
from app.models import Sports,Student,Teacher,Subject
# Create your views here.
def homee(request):
    # context ={
    #     'Student':Student.objects.all(),
    #     'Teacher':Teacher.objects.all(),
    # }
    # context ={
    #     'Student':Student.objects.select_related('game').all(),
    #     'Teacher':Teacher.objects.select_related('sname','sjname').all(),
    # }

    # context ={
    #     'Student':Student.objects.prefetch_related('subject').all()
    # }

    
    s = Student.objects.prefetch_related('subject').all()
    for i in s:
        for j in i.subject.all():
            temp = i
    

    return render(request,'app/home.html')
