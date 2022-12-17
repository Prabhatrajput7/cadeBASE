from changeapp2.models import Custom
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Custom
        fields = ['username', 'email', 'phone','first_name', 'password', 'password2']
        extra_kwargs = {
            'password' : {'write_only': True},
            'email': {'required': True},
            'phone': {'required': True}
        }
    
    def save(self):

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': 'P1 and P2 should be same!'})

        if Custom.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'Email already exists!'})

        if self.validated_data.get('first_name',None):
            account = Custom(email=self.validated_data['email'], username=self.validated_data['username'],
                        phone=self.validated_data['phone'] ,first_name=self.validated_data['first_name'])

        else:
            account = Custom(email=self.validated_data['email'], username=self.validated_data['username'],
                        phone=self.validated_data['phone'])
        account.set_password(password)
        account.save()
        return account