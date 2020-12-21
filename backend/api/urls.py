from django.urls import path, include
from rest_framework import routers

from api.views import Posts, CreateUser, LoginView, UserProfile, AllPostList, UserSearch, PostSearch, PasswordRecovery

# router = routers.DefaultRouter()
# router.register('users', UserViewSets)

urlpatterns = [
    # path('user/list/', UserList.as_view(), name='user_list'),
    # path('user/<pk>/', user_detail, name='user_detail'),
    # path('', include(router.urls)),
    # -----------------------------------------------------------------------

    path('users/', CreateUser.as_view(), name='create_user'),

    #جستوجو در نام کاربری، نام و نام خانوادگی
    #بدون نیاز به احراز هویت
    path('users/search/', UserSearch.as_view()),
    # path('users/password-recovery/',PasswordRecovery.as_view()),
    # دقت شود اگر در روت زیر به جای user
    # از users
    # استفاده کنیم، به صورت پیشفرض از روت users/id استفاده خواهد کرد. و این مشکلی است که با استفاده از
    # ViewSetها
    # قابل رفع می باشد.
    path('users/login/', LoginView.as_view(), name='user_login'),
    # برای تغیر پروفایل
    path('users/login/<int:id>/', UserProfile.as_view(), name='profile'),

    # ------------------------------------------------------------------------

    path('posts/', AllPostList.as_view(), name='post_list'),
    path('posts/search/', PostSearch.as_view(), name='post_search'),
    # چزئیات یک پست را برمیگرداند
    # GETهمه ی پست های یک یوزر خاص را بر میگرداند
    # ایجاد پست جدید برای کاربر خاصPOST
    path('posts/<int:user_id>/', Posts.as_view(), name='post_detail'),

    # GETیک پست از یک یوزر خاص را بر می گرداند.
    # POSTویرایش یک پست از یک یوزر خاص
    # حذف یک پست از یک یوزر خاصِDELETE
    path('posts/<int:user_id>/<post_pk>/', Posts.as_view()),
    # جزئیات یک پست خاص
    # path('posts/detail/<pk>/', PostDetail.as_view(), name='post_detail')
]
