from django.conf.urls import url
from django.urls import path, include, re_path
from rest_framework import routers
from django.contrib.admin.templates import admin
from api.views import (Posts, CreateUser, AllPostList, UserSearch,
                       PostSearch, LoginOrUpdateProfile, PasswordRecovery, reset_password, )

# router = routers.DefaultRouter()
# router.register('users', UserViewSets)

urlpatterns = [
    # path('user/list/', UserList.as_view(), name='user_list'),
    # path('user/<pk>/', user_detail, name='user_detail'),
    # path('', include(router.urls)),
    # -----------------------------------------------------------------------

    path('users/', CreateUser.as_view(), name='create_user'),

    # جستوجو در نام کاربری، نام و نام خانوادگی
    # بدون نیاز به احراز هویت
    path('users/search/', UserSearch.as_view()),
    path('password-recovery/', PasswordRecovery.as_view()),
    url('reset-password/([a-zA-z0-9-_.])+/', reset_password),
    # post لاگین کردن
    # put اپدیت کردن پروفایل
    path('users/login/', LoginOrUpdateProfile.as_view(), name='user_login'),

    # ------------------------------------------------------------------------

    path('posts/', AllPostList.as_view(), name='post_list'),
    path('posts/search/', PostSearch.as_view(), name='post_search'),

    # GETهمه ی پست های یک یوزر خاص را بر میگرداند
    # ایجاد پست جدید برای کاربر خاصPOST
    path('posts/user/', Posts.as_view(), name='post_detail'),

    # GETیک پست از یک یوزر خاص را بر می گرداند.
    # POSTویرایش یک پست از یک یوزر خاص
    # حذف یک پست از یک یوزر خاصِDELETE
    path('posts/user/<post_pk>/', Posts.as_view()),
    # جزئیات یک پست خاص
    # path('posts/detail/<pk>/', PostDetail.as_view(), name='post_detail')
]
