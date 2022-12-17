from rest_framework import serializers
from .models import Post, Vote, Comment
from datetime import datetime
from django.utils.timesince import timesince

class PostSerializer(serializers.ModelSerializer):

    post = serializers.ReadOnlyField(source='post.username')
    votes = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    # comment_set = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='comment-det')

    class Meta:
        model = Post
        # fields = ['id','title','url','post','votes','con','comments']
        fields= '__all__'

    def get_votes(self, object):
        # print('POST',object.title) this is a single instance
        """
        print('POST'+str(post))
        print('VOte'+str(Vote.objects.filter(post=post)))
        Maching id here post=post
        """
        # return Vote.objects.filter(post__title__contains=object.title).count()
        #  below intance only work with relationships
        return Vote.objects.filter(post=object).count()

    def get_comments(self, post):
        l = []
        # print(Comment.objects.filter(post=post))
        # return Comment.objects.filter(post=post).count()
        for i in Comment.objects.filter(post=post):
            l.append(i.comment)
        return l


class CommentSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')
    post = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Comment
        fields = ['id','comment','user','post']        

class VoteSerializer(serializers.ModelSerializer):

    voter = serializers.ReadOnlyField(source='voter.username')
    post = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Vote
        fields = ['voter','post']


    
