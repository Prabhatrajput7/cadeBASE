import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','crash.settings')

import django
django.setup()

#data
from fack.models import Webpage,AccessRec,Topic
import random
from faker import Faker

ff = Faker()

topic = ['solarsystem','ootcloud','blackhole','milkyway','mars','earth','jupiter','saturn']

def add_topic():
    t = Topic.objects.get_or_create(name = random.choice(topic))[0]
    tt = Topic.objects.get_or_create(name = random.choice(topic))
    print('T',t)
    print('TT',tt)
    t.save()
    return t

def population(n=5):
    for i in range(n):
        t = add_topic()
        fakeurl = ff.url()
        fakegen = ff.date()
        cname = ff.company()

        web = Webpage.objects.get_or_create(topic=t,name=cname,url = fakeurl)[0]
        accR =AccessRec.objects.get_or_create(webpg=web,data=fakegen)[0]

if __name__=='__main__':
    print('Popualation')
    population()
    print('Done')