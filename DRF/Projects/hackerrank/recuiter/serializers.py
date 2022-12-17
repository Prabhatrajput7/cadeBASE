from numpy import source
from userd.models import JD, Application
from rest_framework import serializers

class Jdser(serializers.ModelSerializer):

    posted_by = serializers.ReadOnlyField(source='rec.username')

    class Meta:
        model = JD
        exclude = ('rec',)


class ApplicationSer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = '__all__'            