import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','papa.settings')

import django
django.setup()

from django.core.management import BaseCommand
from django_redis import get_redis_connection

from app.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        con = get_redis_connection("default")

        ambassadors = User.objects.filter(is_ambassador=True)
        # print(ambassadors)
        for ambassador in ambassadors:
            # print(ambassador.name, float(ambassador.revenue))
            con.zadd('rankings', {ambassador.name: float(ambassador.revenue)})


if __name__ == '__main__':
    c = Command()
    c.handle()