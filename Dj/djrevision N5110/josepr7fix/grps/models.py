from django.conf import settings
from django.urls import reverse
from django.db import models
from django.utils.text import slugify
# from accounts.models import User
# https://www.youtube.com/watch?v=-HuTlmEVOgU&t=857s
import misaka
from django.contrib.auth import get_user_model
User = get_user_model()
# https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/#inclusion-tags
# This is for the in_group_members check template tag
from django import template
register = template.Library()



class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User,through="GroupMember")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("grps:single", kwargs={"slug": self.slug})


    class Meta:
        ordering = ["name"]


class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name="memberships",on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='user_groups',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("group", "user")


"""
>>> from grps.models import Group,GroupMember
>>> g = Group.objects.get(slug='dogs')
>>> g
<Group: Dogs>
>>> g.members
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x000002A5DE091AF0>
>>> g.members.all()
<QuerySet [<User: test123>, <User: viggy>]>
>>> g.members.all()[0]
<User: test123>
>>> gm = GroupMember.objects.get(id=3)
>>> gm
<GroupMember: viggy>
>>> gm.user
<User: viggy>
>>> gm.user.username
'viggy'
>>> g
<Group: Dogs>
>>> g.memberships
<django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x000002A5DE1DB820>
>>> g.memberships.all()
<QuerySet [<GroupMember: test123>, <GroupMember: viggy>]>
>>> exit()
"""