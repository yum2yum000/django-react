import re
from random import random

from django.core.mail import send_mail
from django.db.models import Q
from django.db.utils import IntegrityError

from django.contrib.auth import authenticate, password_validation
from django.contrib.auth.models import update_last_login
from django.core.validators import EmailValidator, validate_email
from django.template.loader import get_template
from rest_framework import viewsets, status, serializers
from rest_framework import generics
from rest_framework.authtoken.models import Token
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api._serializer import UserSerializer, PostSerializer
from first import settings
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
            email = email.lower()
            # چک کردن اینکه ایمیل تکراری وارد نشود
            try:
                # ایمیل تکراری است
                CustomUser.objects.get(email=email)
                return Response({'email': 'email does exists'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            except:
                pass
            try:
                validate_email(email)
                user.email = email
            except Exception as err:
                # فرمت ایمیل درست نیست
                return Response({'email': err}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # فیلد ایمیل لازم است
            return Response({'email': 'Required'}, status=status.HTTP_411_LENGTH_REQUIRED)
        # password validate
        try:
            password_validation.validate_password(data.get('password'))
        except ValidationError as err:
            return Response({'password': err}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        data = request.data

        if self.validate(data):
            return self.validate(data)

        user = CustomUser(
            username=data.get('username').lower(),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email').lower(),
            adres=data.get('adres'),
            bio=data.get('bio'),
            avatar=data.get('avatar'),
            phone=data.get('phone'),
        )
        user.set_password(data.get('password'))
        user.save()
        Token.objects.create(user=user)
        data = self.get_serializer(user).data
        return Response({'user': data})

    # def post(self, request):


class LoginOrUpdateProfile(APIView):
    serializer_class = UserSerializer

    # لاگین شدن
    def post(self, request):
        username = request.data.get('username').lower()
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            update_last_login(None, user)
            return Response({'token': user.auth_token.key, 'id': user.id}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Wrong Credentials'}, status=status.HTTP_400_BAD_REQUEST)

    # اپدیت پروفایل
    def put(self, request):
        # توکن ارسالی مربوط به ای دی ارسالی می باشد و این کاربر مجاز به تغییرات در پروفایل است
        # if request.data.get('phone').isdigit() is not True:
        #     raise serializers.ValidationError({'error': 'Phone is not digit'})
        id = request.user.id
        if id:
            user = CustomUser.objects.get(id=id)
            update = request.data.get('update').lower()
            if update == "data":
                return self.update_data(request, user)
            elif update == 'password':
                return self.update_password(request, user)
            else:
                return Response({'user': UserSerializer(user).data}, status=status.HTTP_200_OK)

        return Response(data={'user': 'Forbiden', 'detail': 'This user not matched with token string'},
                        status=status.HTTP_403_FORBIDDEN)

    def update_data(self, request, user):
        # update all data except the password
        # update all infoes
        data = request.data
        if data.get('username'):
            # اگر نام درخواستی برای تغییر در دیتابیس باشد، تغییر امکان پذیر نیست
            try:
                # اگر خط زیر دست اجرا شود، پس نمیتوان نام  کاربری درخواستی را به یوزر نسبت داد. چون همچین نامی وجود دارد
                CustomUser.objects.get(username=data.get('username').lower())
                return Response(data={'username': 'user name does exists'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            except:
                # اگر نام کاربری درخواستی در دیتابیس نباشد، می توان تغییرداد
                user.username = data.get('username').lower()

        # email validate
        email = data.get('email').lower()
        if email:
            # چک کردن اینکه ایمیل تکراری وارد نشود
            try:
                # ایمیل تکراری است
                # اگر ایمیل وارد شده مربوط به کاربر حاضر نباشد. نمی توان این ایمیل را به کاربر دیگر تخصیص داد پس
                if CustomUser.objects.get(email=email).id != user.id:
                    return Response({'email': 'email does exists'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            except:
                # اگر ایمیل وارد شده در دیتابیس نباشد پس می توان ایمیل کاربر حاضر را به آن تغغیر داد
                pass
            try:
                validate_email(email)
                user.email = email
            except Exception as err:
                # فرمت ایمیل درست نیست
                return Response({'email': err}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # فیلد ایمیل لازم است
            return Response({'email': 'Required'}, status=status.HTTP_411_LENGTH_REQUIRED)

        user.first_name = data.get('first_name') or user.first_name
        user.last_name = data.get('last_name') or user.last_name
        user.adres = data.get('adres') or user.adres
        user.bio = data.get('bio') or user.bio
        user.avatar = data.get('avatar') or user.avatar
        user.phone = data.get('phone') or user.phone

        user.save()
        return Response(data={'data': 'updated', "user": UserSerializer(user).data}, status=status.HTTP_200_OK)

    def update_password(self, request, user):
        try:
            password_validation.validate_password(request.data.get('password'))
        except Exception as err:
            return Response({'password': err}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(request.data.get('password'))
        return Response({'password': 'updated'}, status=status.HTTP_200_OK)


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
    def get(self, request, post_pk=None):
        # زمانی که این متد فراخوانی شود یعنی توکن تایید شده است و
        # request.user
        # در دسترس قرار می گیرد.

        # اگر ای دی کاربر با ای دی توکن یکسان باشد
        if request.user.id:
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

    def post(self, request):
        """
        برای ذخیره کردن پست های کاربر خاصی از این متد استفاده می شود
        توجه شود که می توان درخواست های زیادی را پی در پی فرستاد که این موجب اخلال درکار وب سرویس خواهد کرد
        برای جلوگیری از این اتفاق باید یک timespan قرار داده شود.
        در production حتما این کار انجام شود.
        :param request:
        :return:
        """
        # اگر توکن وارد شده در صحیح باشد
        if request.user.id:
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
    def put(self, request, post_pk):
        if request.user.id:
            post = get_object_or_404(Post, pk=post_pk)
            post.title = request.data.get('title') or post.title
            post.content = request.data.get('content') or post.content
            post.save()
            data = PostSerializer(post).data
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(data={'user': 'Invalid'}, status=status.HTTP_400_BAD_REQUEST)

    # delete post
    def delete(self, request, post_pk):
        if request.user.id:
            post = get_object_or_404(Post, pk=post_pk)
            post.delete()
            return Response({'post': 'deleted'}, status=status.HTTP_200_OK)
        else:
            return Response(data={'user': 'Invalid'}, status=status.HTTP_400_BAD_REQUEST)


class UserSearch(APIView):

    def get(self, request):
        data = request.data
        if data.get('search'):
            users = CustomUser.objects.filter(Q(username__contains=data.get('search')) |
                                              Q(first_name__contains=data.get('search')) |
                                              Q(last_name__contains=data.get('search'))).all()
            data_serialized = UserSerializer(users, many=True).data
            return Response(data_serialized, status=(status.HTTP_200_OK if users.count() > 0 else status.HTTP_404_NOT_FOUND))
        else:
            return Response({'search': 'Invalid value'}, status=status.HTTP_400_BAD_REQUEST)


class PostSearch(APIView):
    def get(self, request):
        data = request.data
        if data.get('search'):
            posts = Post.objects.filter(Q(title__contains=data.get('search')) | Q(content__contains=data.get('search')))
            data_serialized = PostSerializer(posts, many=True).data
            # اگر چیزی پیدا نشود، 404 ارسال می کند.
            return Response(data_serialized, status=(status.HTTP_200_OK if posts.count() > 0 else status.HTTP_404_NOT_FOUND))
        else:
            # اگر دیتا ارسال نشود 400 ارسال می کند.
            return Response({'search': 'Invalid value'}, status=status.HTTP_400_BAD_REQUEST)


class PasswordRecovery(APIView):

    def password_generator(self):
        s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
        length = random.randrange(8, 12)
        passowrd = ''
        for p in range(length):
            passowrd += random.choice(s)
        return passowrd

    def get(self, request):
        data = request.data

        try:
            email = data.get('email').lower()
            user = CustomUser.objects.get(email=email)
            # send email
            # مقادیر ارسالی مانند رمز عبور جدید و... را در قالب template قرار می دهد.
            password = self.password_generator()
            user.set_password(password)
            rendered_message = get_template('password_recovery.html').render({
                'password': password, 'username': user.username
            })
            # fail_silently=True
            # پیش فرض False
            # اگر مقدار این False باشد، خطاهایی که هنگام ارسال ایمیل می تواند رخ دهد را نشان می دهد.
            # smtplib.SMTPException
            #
            # hmtl_message
            # اگر متن پیام از طریق این ارسال شود، به صورت یک سند html فرض شده، و تگهای html و کدهای css در ایمیل اجرا خواهند شد
            # اگر از طریق این ارسال نشود، تگها و کدها خود جزوی از متن پیام اسلی تلقی می شود.
            send_mail(subject='بازیابی رمز عبور', message='', from_email=settings.EMAIL_HOST_USER,
                      recipient_list=(email,),
                      fail_silently=True,
                      html_message=rendered_message)
        except:
            return Response({'email': 'email does not exists'}, status=status.HTTP_404_NOT_FOUND)
