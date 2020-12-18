from django.urls import path, include
from rest_framework import routers

from api.views import PostList, UserViewSets

router = routers.DefaultRouter()
router.register('users', UserViewSets)

urlpatterns = [
    # path('user/list/', UserList.as_view(), name='user_list'),
    # path('user/<pk>/', user_detail, name='user_detail'),
    path('', include(router.urls)),
    path('post/list/', PostList.as_view(), name='post_list'),
]
