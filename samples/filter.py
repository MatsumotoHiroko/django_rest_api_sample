from django_filters import rest_framework as filters 
from samples.models import Posts, Users, Categories

class PostsFilter(filters.FilterSet):
    class Meta:
        model = Posts
        fields = ['title'] 
class UsersFilter(filters.FilterSet):
    class Meta:
        model = Users
        fields = ['name']         
class CategoriesFilter(filters.FilterSet):
    class Meta:
        model = Categories
        fields = ['name']                 