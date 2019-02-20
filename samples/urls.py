from django.conf.urls import include, url
from rest_framework import routers
from samples.views import index, PostsViewSet, UsersViewSet, CategoriesViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostsViewSet)
router.register(r'users', UsersViewSet)
router.register(r'categories', CategoriesViewSet)


urlpatterns = [
    url(r'api/', include(router.urls)),
    url(r'', index, name='index'),
]