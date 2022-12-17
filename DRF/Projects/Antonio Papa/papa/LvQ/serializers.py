from rest_framework import serializers
from .models import LQ

class SLQ(serializers.ModelSerializer):

    class Meta:
        model = LQ
        fields = "__all__"