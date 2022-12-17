from pyexpat import model
from rest_framework import serializers
from .models import User

class RegSer(serializers.ModelSerializer):

    password = serializers.CharField(style={'input_type':'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username','email', 'first_name', 'last_name','gender','password','password2']   

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': 'P1 and P2 should be same!'})

        account = User(username = self.validated_data['username'],email=self.validated_data['email'],
                        first_name = self.validated_data['first_name'],last_name = self.validated_data['last_name'],
                        gender=self.validated_data['gender'])
        s = self.context.get('is_seeker')
        r = self.context.get('is_rec')
        account.is_seeker = s
        account.is_rec = r
        account.set_password(password)
        account.save()
        return account 


class LoginSer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=255)
    password = serializers.CharField(style={'input_type':'password'})
    class Meta:
        model = User
        fields = ['username', 'password']       


class ProfileSer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password','groups','user_permissions',)

class ProfileUpdate(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email']

            
class PasswordChg(serializers.Serializer):

    password = serializers.CharField(max_length=255, style={'input_type':'password'})
    password2 = serializers.CharField(max_length=255, style={'input_type':'password'})
    class Meta:
        fields = ['password', 'password2']
