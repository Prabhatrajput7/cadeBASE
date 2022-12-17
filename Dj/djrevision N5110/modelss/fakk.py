import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','modelss.settings')

import django
django.setup()

#data
from app.models import Sports,Student,Teacher,Subject
import random
from faker import Faker

ff = Faker()

sub = ['sst','science','eng','cs']
sp = ['tt','footbal','cricket','esports']

def add_sp():
    s = Sports.objects.get_or_create(gname = random.choice(sp))[0]
    return s

def add_sub():
    sb = Subject.objects.get_or_create(sname = random.choice(sub))[0]
    return sb

def population():
    for i in range(300,1000):
        s = add_sp()
        sb = add_sub()

        stu = Student(name= ff.name(),rollno=i,game=s)
        stu.save()
        Teacher.objects.create(tname= ff.name(),sname=stu,sjname=sb)

if __name__=='__main__':
    print('Popualation')
    population()
    print('Done')