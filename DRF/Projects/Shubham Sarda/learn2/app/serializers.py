from rest_framework import serializers
from app.models import Movie



# class MovieSerial(serializers.ModelSerializer):

#     len_name = serializers.SerializerMethodField()
#     """custom serilizer fields"""

#     class Meta:
#         model = Movie
#         """this will be filled that displayed on web"""
#         fields = '__all__'

#     def get_len_name(self,object):
#         """object is a model"""
#         return len(object.name)



"""Hyperlink"""

class MovieSerial(serializers.HyperlinkedModelSerializer):

    # platform = serializers.SerializerMethodField()
    len_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'   

    def get_len_name(self,object):
        return len(object.name)
    
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short!")
        else:
            return value




# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short!")

# class MovieSerial(serializers.Serializer):
#     """is will display this on web page"""
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """instance is old and validated is now data"""
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Title and Description should be different!")
    #     else:
    #         return data

    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     else:
    #         return value