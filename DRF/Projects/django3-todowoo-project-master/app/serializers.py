from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    datecompleted = serializers.ReadOnlyField()
    user  = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = ['id','title','memo','created','datecompleted','important','user']

    def get_user(self,object):
        return object.user.username

class TodoCompleteSerializer(serializers.ModelSerializer):

    title = serializers.SerializerMethodField()
    
    class Meta:
        model = Todo
        fields = ['id','title']
        # read_only_fields = ['memo','created','datecompleted','important','title']

    def get_title(self,object):
        return object.title