from .models import Comment, PostLike, PostTag, Tag, User, Userprofile
from .models import Category
from .models import Post
from rest_framework import serializers

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields ='__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields ='__all__'
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields ='__all__'
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comment
        fields="__all__"
        
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= Userprofile
        fields = "__all__"

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields= "__all__"
        
class PostTagSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostTag
        fields= "__all__"

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostLike
        fields= "__all__"