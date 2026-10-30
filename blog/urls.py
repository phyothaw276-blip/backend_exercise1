from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from .models import *
from .serializers import *
from rest_framework import viewsets

router = DefaultRouter()
router.register(r'users', UserViewset, basename='user')  
router.register(r'categories', CategoriyViewSet, basename='category')
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'userprofiles', UserProfileViewSet, basename='userprofile')
router.register(r'tags', TagViewSet, basename='tag')    
router.register(r'posttags', PostTagViewSet, basename='posttag' )
router.register(r'postlikes', PostLikeViewSet, basename='postlike')
urlpatterns = [
    path('', include(router.urls)),
]