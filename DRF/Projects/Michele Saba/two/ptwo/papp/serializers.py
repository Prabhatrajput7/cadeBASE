from rest_framework import serializers
from .models import Profile,ProfileStatus

class ProfileSerial(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only = True)
    avatar = serializers.ImageField(read_only = True)

    class Meta:
        model = Profile
        fields = '__all__'

class ProfileAvatarSerial(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('avatar',)

class ProfileStatusSerial(serializers.ModelSerializer):
    
    user_profile = serializers.StringRelatedField(read_only=True) 

    class Meta:
        model = ProfileStatus
        fields = '__all__'
      