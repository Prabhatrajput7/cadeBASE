#serialization converting db obj to json format or any ther obj deserization is visevarse

from attr import field
from rest_framework import serializers
from .models import HariOne

class HariSerializers(serializers.ModelSerializer):
    class Meta:
        model = HariOne
        fields = '__all__'
        