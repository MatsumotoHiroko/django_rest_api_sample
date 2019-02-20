from rest_framework import serializers
from samples.models import Posts, Users, Categories

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        exclude = ()

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        exclude = ()

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        exclude = ()
