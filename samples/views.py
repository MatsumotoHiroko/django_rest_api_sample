from django.shortcuts import render
from django.conf import settings
from django.http.response import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import generics
from rest_framework.response import Response
from samples.models import Posts, Users, Categories
from samples.serializer import  PostsSerializer, UsersSerializer, CategoriesSerializer
from samples.pagination import PostsPagination, UsersPagination, CategoriesPagination
from samples.filter import PostsFilter, UsersFilter, CategoriesFilter
import os

# 静的ファイルを返すView
def index(_):
    html = open(
        os.path.join(settings.STATICFILES_DIRS[0], "dist/index.html")).read()
    return HttpResponse(html)

class PostsViewSet(viewsets.ModelViewSet):
    """
    get:
    """    
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    filter_class = PostsFilter
    ordering_fields = ('created_at')
    pagination_class = PostsPagination            

class UsersViewSet(viewsets.ModelViewSet):
    """
    get:
    """    
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    filter_class = UsersFilter
    ordering_fields = ('created_at')
    pagination_class = UsersPagination            

class CategoriesViewSet(viewsets.ModelViewSet):
    """
    get:
    """    
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    filter_class = CategoriesFilter
    ordering_fields = ('created_at')
    pagination_class = CategoriesPagination            