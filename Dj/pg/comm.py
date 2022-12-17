"""
Change DB

1.python manage.py dumbdata --exclude auth.permission --exclude contenttypes > data.json
2. settings.py database ={
    'deafult',
    'nem
}
3. python manage.py loaddata data.json --databse=new

-OR-

1.python manage.py dumbdata > data.json
2. clear contentype open shell
from django.contrib.contenttypes.models import Contentype
Contentype.objects.all.delete()
3.python manage.py loaddata data.json

"""

"""
Session DJ

request.session['name'] = 'Viggy'
request.session.get('name',None)
request.session.set_expiry(1)

Template side- {{request.session.name}} will print vigil

from django.contrib.sessions.models import Session
admin.site.registe(Session)

python manage.py clearsessions

- To change the session stroage to cookie use 

sessionengine in settings.py
SESSION_ENGINE = "django.contrib.sessions.backends.cache" 

cokiee uses secret key of django that is not secire way to generate cookie

img for session engine and cache table

check DJ doc for more cache and session

"""

"""
for
        <div class="form-control {% if cf.errors %}invalid{% endif %}">
            {{cf.label_tag}}
            {{cf}}
            {{cf.errors}}
        </div>
endfor
"""

# name mingling
# class A:
# __a = 5
# print(A._A.__a)

"""
multi database 
default 
new

python manage.py migrate --database new
.save(using='new)
.all().using('new')
"""

# django-simple-history
# django-extension {work like a shell plus}
# sentry code fata to mail aa jaega
# https://www.youtube.com/shorts/F7BQxNayERo
