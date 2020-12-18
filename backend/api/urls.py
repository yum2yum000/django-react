from django.urls import path, include
from rest_framework import routers

from api.views import PostList, CreateUser, LoginView, UserProfile

# router = routers.DefaultRouter()
# router.register('users', UserViewSets)

urlpatterns = [
    # path('user/list/', UserList.as_view(), name='user_list'),
    # path('user/<pk>/', user_detail, name='user_detail'),
    # path('', include(router.urls)),
    # -----------------------------------------------------------------------

    path('users/', CreateUser.as_view(), name='create_user'),
    # دقت شود اگر در روت زیر به جای user
    # از users
    # استفاده کنیم، به صورت پیشفرض از روت users/id استفاده خواهد کرد. و این مشکلی است که با استفاده از
    # ViewSetها
    # قابل رفع می باشد.
    path('users/login/', LoginView.as_view(),name='user_login'),
    # برای تغیر پروفایل
    path('users/login/<int:id>/', UserProfile.as_view(), name='profile'),

    # ------------------------------------------------------------------------
    # لیست کردن پست های کاربر خاص
    # نیاز به توکن

    path('posts/list/', PostList.as_view(), name='post_list'),
    #چزئیات یک پست را برمیگرداند
    path('posts/list/<int:pk>/', PostList.as_view(), name='post_detail'),
    # جزئیات یک پست خاص
    # path('posts/detail/<pk>/', PostDetail.as_view(), name='post_detail')
]
