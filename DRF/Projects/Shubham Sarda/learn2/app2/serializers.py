from rest_framework import serializers
from app2.models import StreamPlatform,WatchList,Review

class ReviewSerializerzMVS(serializers.ModelSerializer):

    review_user = serializers.SerializerMethodField()
    watchlist = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = '__all__'
    
    def get_watchlist(self,object):
        return object.watchlist.title

    def get_review_user(self,object):
        return object.review_user.username

class ReviewSerializerz(serializers.ModelSerializer):

    reviewby = serializers.SerializerMethodField()
    moviename = serializers.SerializerMethodField()

    class Meta:
        model = Review
        exclude = ('review_user',)
    
    def get_moviename(self,object):
        return object.watchlist.title

    def get_reviewby(self,object):
        return object.review_user.username

class WatchListSerialz(serializers.ModelSerializer):

    reviews = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='app2:reviewind-detail')
    watchon = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        fields = '__all__'   

    def get_watchon(self,object):
        return object.platform.name

class StreamSerialz(serializers.ModelSerializer):

    # watchlist = WatchListSerialz(many=True, read_only=True)
    """watchlist name is very imp as we used this in related_name=watchlist this will return completed data"""

    # watchlist = serializers.StringRelatedField(many=True)
    """this will return only __str__ data"""

    watchlist = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='app2:watchlist-detail')
    """for hyperling details of individual in list  HERE watchlist is the related name"""
    # https://www.youtube.com/watch?v=ZA-O6r5UvdI


    class Meta:
        model = StreamPlatform
        fields = '__all__'
        # read_only_fields = ['a','b']










"""Hyperlink"""

# class WatchListSerialz(serializers.HyperlinkedModelSerializer):

#     platform = serializers.SerializerMethodField()

#     class Meta:
#         model = WatchList
#         fields = '__all__'   

#     def get_platform(self,object):
#         return object.platform.name

# class StreamSerialz(serializers.HyperlinkedModelSerializer):

#     watchlist = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='app2:streamplatform-detail')

#     class Meta:
#         model = StreamPlatform
#         fields = '__all__'   

