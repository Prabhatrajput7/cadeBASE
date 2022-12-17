from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogapp:detail', kwargs={'pk': self.pk})

"""
with open('corey.json') as f:
   ...:     js = json.load(f)
for j in js:
   ...:     Post.objects.create(title=j['title'],content=j['content'], author_id=j['user_id'])
"""        

class Comment(models.Model):
    reply = models.ForeignKey('comment', on_delete=models.CASCADE, null=True, related_name='replies')
    cby = models.ForeignKey(User, on_delete=models.CASCADE)
    pst = models.ForeignKey(Post,on_delete=models.CASCADE,blank=True,null=True)
    com_posted = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return f'{self.id} , {self.cby.username}'

# class Reply(models.Model):
#     comment_name = models.ForeignKey(Comment, on_delete=models.CASCADE,related_name='replies')
#     reply_body = models.TextField(max_length=500)
#     author = models.ForeignKey(User,on_delete=models.CASCADE)
#     com_posted = models.DateTimeField(default=timezone.now)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return "reply to " + str(self.comment_name)        