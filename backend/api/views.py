import re

from django.db.models import Q
from django.db.utils import IntegrityError

from django.contrib.auth import authenticate, password_validation
from django.contrib.auth.models import update_last_login
from django.core.validators import EmailValidator, validate_email
from rest_framework import viewsets, status, serializers
from rest_framework import generics
from rest_framework.authtoken.models import Token
from django.core.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api._serializer import UserSerializer, PostSerializer
from post.models import CustomUser, Post


# class UserList(ListAPIView):
#     serializer_class = UserSerializer
#     queryset = CustomUser.objects.all()
#
# def user_detail(pk):
#     user=get_object_or_404(CustomUser, pk=pk)
#     return user

# class UserViewSets(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer


# class PostList(ListAPIView):
#     permission_classes = (IsAuthenticated,)
#
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#
#     class Meta:
#         model = Post
#         fields = '__all__'


class CreateUser(generics.CreateAPIView):
    # این دو کلاس به صورت پیش فرش در فایل settings.py تعریف شده است
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

    def validate(self, data):
        if data.get('username') is None or data.get('password') is None:
            return Response({'username or password': 'Not valid'}, status=status.HTTP_400_BAD_REQUEST)
        user = CustomUser()
        # username validate
        try:
            # اگر نام وارد شده وجود داشته باشد خط return اجرا خواهد شد. و اگر نداشته باشد خط return اجرا نشده و ثبت نام کابر به صورت عادی طی خواهد شد.
            user = CustomUser.objects.get(username=data.get('username'))
            return Response({'username': 'user name does exists'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        except:
            pass

        # phone validate
        if data.get('phone'):
            if re.match('^09[0-9]{9}$', data.get('phone')) is None:
                return Response({'phone': 'Not valid'}, status=status.HTTP_400_BAD_REQUEST)

        # email validate
        email = data.get('email')
        if email:
            try:
                validate_email(email)
                user.email = email
            except Exception as err:
                return Response({'email': err}, status=status.HTTP_400_BAD_REQUEST)

        # password validate
        try:
            password_validation.validate_password(data.get('password'))
        except ValidationError as err:
            return Response({'error': err}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        data = request.data

        if self.validate(data):
            return self.validate(data)

        user = CustomUser(
            username=data.get('username'),
            phone=data.get('phone'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            adres=data.get('adres'),
            bio=data.get('bio'),
            avatar=data.get('avatar'),
        )
        user.set_password(data.get('password'))
        user.save()
        Token.objects.create(user=user)
        data = self.get_serializer(user).data
        return Response({'user': data})

    # def post(self, request):


#
# def get(self, request):
#     if request.method.POST:
#         username = request.POST['username']
#         password = request.POST['password']
#         data = UserViewSets((username, password)).data
#         return Response(data)


class UserProfile(APIView):
    permission_classes = (IsAuthenticated,)

    # یک توکن و یک ای دی دریافت می شود. در صورتی که توکن مربوط به ای دی باشد اپدیت انجام می شود.
    def put(self, request, id):
        # توکن ارسالی مربوط به ای دی ارسالی می باشد و این کاربر مجاز به تغییرات در پروفایل است
        # if request.data.get('phone').isdigit() is not True:
        #     raise serializers.ValidationError({'error': 'Phone is not digit'})
        if request.user.id == id:
            user = CustomUser.objects.get(id=id)
            update = request.data.get('update').lower()
            if update == "data":
                return self.update_data(request, user)
            elif update == 'password':
                return self.update_password(request, user)
            else:
                return Response({'user': UserSerializer(user).data}, status=status.HTTP_200_OK)

        return Response(data={'update': 'Forbiden', 'detail': 'This user not matched with token string'},
                        status=status.HTTP_403_FORBIDDEN)

    def update_data(self, request, user):
        # update all data except the password
        # update all infoes
        data = request.data
        user.first_name = data.get('first_name') or user.first_name
        user.last_name = data.get('last_name') or user.last_name
        user.adres = data.get('adres') or user.adres
        user.bio = data.get('bio') or user.bio
        user.avatar = data.get('avatar') or user.avatar
        user.phone = data.get('phone') or user.phone

        # email validation
        email = data.get('email')
        if email:
            try:
                validate_email(email)
                user.email = email
            except Exception as err:
                return Response({'email': err}, status=status.HTTP_400_BAD_REQUEST)

        # user.set_password(request.data.get('password'))
        # user = UserSerializer(request.data).data
        # if user.is_valid():
        user.save()
        return Response(data={'update': 'Ok', "user": UserSerializer(user).data}, status=status.HTTP_200_OK)

    def update_password(self, request, user):
        try:
            password_validation.validate_password(request.data.get('password'))
        except Exception as err:
            return Response({'non_field_errors': err}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(request.data.get('password'))
        return Response({'password': 'updated'}, status=status.HTTP_200_OK)


class LoginView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            update_last_login(None, user)
            return Response({'token': user.auth_token.key, 'id': user.id}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Wrong Credentials'}, status=status.HTTP_400_BAD_REQUEST)


# class PostList1(generics.ListAPIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()


class AllPostList(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class Posts(APIView):
    permission_classes = (IsAuthenticated,)

    # درخواست لیست پست ها
    def get(self, request, user_id=None, post_pk=None):
        # زمانی که این متد فراخوانی شود یعنی توکن تایید شده است و
        # request.user
        # در دسترس قرار می گیرد.

        # اگر ای دی کاربر با ای دی توکن یکسان باشد
        if request.user.id == user_id:
            objs = Post.objects.filter(user_id=request.user.id)

            if post_pk:
                # اگر پست خاصی مد نظر باشد.
                objs = get_object_or_404(objs, pk=post_pk)
                # اگر پست خاص پیدا نشود.
            data = PostSerializer(objs, many=not post_pk).data
            return Response(data, status=status.HTTP_200_OK)
        else:
            # همه ی پست های یک کاربر داده می شود
            return Response({'user': 'Token or user id invalid'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, user_id):
        """
        برای ذخیره کردن پست های کاربر خاصی از این متد استفاده می شود
        توجه شود که می توان درخواست های زیادی را پی در پی فرستاد که این موجب اخلال درکار وب سرویس خواهد کرد
        برای جلوگیری از این اتفاق باید یک timespan قرار داده شود.
        در production حتما این کار انجام شود.
        :param request:
        :return:
        """
        if request.user.id == user_id:
            # create post
            title = request.data.get('title')
            content = request.data.get('content')
            # فیلدهای title و content هم باید ارسال شوند و هم باید مقدار داشته باشند.
            if title is None or content is None or title.strip() == "" or content.strip() == "":
                return Response({'post': 'title or content is empty'}, status=status.HTTP_400_BAD_REQUEST)

            user = request.user
            title = request.data.get('title')
            content = request.data.get('content')
            try:
                post = Post(user=user, title=title, content=content)
                post.save()
            except:
                return Response({'post': 'post title is duplicated'}, status=status.HTTP_400_BAD_REQUEST)
            return Response(data={'id': post.pk, 'save': 'Ok'}, status=status.HTTP_201_CREATED)
        else:
            return Response(data={'user': 'Invalid'}, status=status.HTTP_400_BAD_REQUEST)

    # update post
    def put(self, request, user_id, post_pk):
        if request.user.id == user_id:
            post = get_object_or_404(Post, pk=post_pk)
            post.title = request.data.get('title') or post.title
            post.content = request.data.get('content') or post.content
            post.save()
            data = PostSerializer(post).data
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(data={'user': 'Invalid'}, status=status.HTTP_400_BAD_REQUEST)

    # delete post
    def delete(self, request, user_id, post_pk):
        if request.user.id == user_id:
            post = get_object_or_404(Post, pk=post_pk)
            post.delete()
            return Response({'post': 'deleted'}, status=status.HTTP_200_OK)
        else:
            return Response(data={'user': 'Invalid'}, status=status.HTTP_400_BAD_REQUEST)


class SearchUser(APIView):

    def get(self, request):
        data = request.data
        if data.get('content'):
            users = CustomUser.objects.all()
            # users = CustomUser.objects.filter(first_name__contains=first_name).all()
            # users = CustomUser.objects.filter(last_name__contains=last_name).all()

            data = UserSerializer(users, many=(users.count() - 1 == True)).data if users.count() > 0 else {'search': 'Not Found'}
            return Response(data, status=(status.HTTP_200_OK if users.count() > 0 else status.HTTP_404_NOT_FOUND))
        else:
            return Response({'search': 'Invalid value'}, status=status.HTTP_400_BAD_REQUEST)
