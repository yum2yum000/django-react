from django.urls import path, include
from rest_framework import routers

from api.views import PostList, PostDetail, CreateUser, LoginView, UserProfile

# router = routers.DefaultRouter()
# router.register('users', UserViewSets)

urlpatterns = [
    # path('user/list/', UserList.as_view(), name='user_list'),
    # path('user/<pk>/', user_detail, name='user_detail'),
    # path('', include(router.urls)),

    path('users/', CreateUser.as_view(), name='create_user'),
    #برای تغیر پروفایل
    path('users/<id>/', UserProfile.as_view()),
    #دقت شود اگر در روت زیر به جای user
    # از users
    #استفاده کنیم، به صورت پیشفرض از روت users/id استفاده خواهد کرد. و این مشکلی است که با استفاده از
    #ViewSetها
    #قابل رفع می باشد.
    path('user/login/', LoginView.as_view()),
    path('post/list/<id>/', PostList.as_view(), name='post_list'),
    path('post/detail/<pk>/', PostDetail.as_view(), name='post_detail')
]
