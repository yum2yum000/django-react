from django.urls import path, include
from rest_framework import routers

from api.views import PostList, UserViewSets, PostDetail, CreateUser

router = routers.DefaultRouter()
router.register('users', UserViewSets)

urlpatterns = [
    # path('user/list/', UserList.as_view(), name='user_list'),
    # path('user/<pk>/', user_detail, name='user_detail'),
    path('', include(router.urls)),
    path('user/create/', CreateUser.as_view(), name='create_user'),
    path('post/list/', PostList.as_view(), name='post_list'),
    path('post/detail/<pk>/', PostDetail.as_view(), name='post_detail')
]
