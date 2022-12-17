import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','blog.settings')

import django
django.setup()

#data
from blogapp.models import Post
import random
from faker import Faker

ff = Faker()

topic = ['solarsystem','ootcloud','blackhole','milkyway']

def population(n=5):
    for _ in range(n):
        titlep = ff.word()
        contentp = ff.sentence()
        userid = random.randint(1,10)
        Post.objects.create(title=titlep ,content= contentp, author_id=userid)

if __name__=='__main__':
    print('Popualation')
    population()
    print('Done')