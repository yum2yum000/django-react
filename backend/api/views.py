from django.contrib.auth import authenticate, password_validation
from rest_framework import viewsets, status, serializers
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.test import force_authenticate
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

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
            update = request.data.get('update')
            if update == "data":
                return self.update_data(request, user)
            elif update == 'password':
                return self.update_password(request, user)
            else:
                return Response({'user': UserSerializer(user).data}, status=status.HTTP_200_OK)

        return Response(data={'update': 'Forbiden', 'detail': 'This user not matched with token string'},
                        status=status.HTTP_403_FORBIDDEN)

    def validate(self, data):
        return True

    def update_data(self, request, user):
        # update all data except the password
        # update all infoes
        user.phone = request.data.get('phone')
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
            return Response({'token': user.auth_token.key, 'id': user.id}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Wrong Credentials'}, status=status.HTTP_400_BAD_REQUEST)


# class PostList1(generics.ListAPIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()


class Posts(APIView):
    permission_classes = (IsAuthenticated,)

    # درخواست لیست پست ها
    def get(self, request, pk=None):
        # زمانی که این متد فراخوانی شود یعنی توکن تایید شده است و
        # request.user
        # در دسترس قرار می گیرد.

        # لیست کل پست ها
        if pk is None:
            # همه ی پست های یک کاربر داده می شود
            objs = Post.objects.filter(user_id=request.user.id)
            data = PostSerializer(objs, many=True).data
            return Response(data, status=status.HTTP_200_OK)
        else:
            # محتوای یک پست داده می شود.
            obj = get_object_or_404(Post, user_id=request.user.id, pk=pk)
            data = PostSerializer(obj).data
            return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        برای ذخیره کردن پست های کاربر خاصی از این متد استفاده می شود
        توجه شود که می توان درخواست های زیادی را پی در پی فرستاد که این موجب اخلال درکار وب سرویس خواهد کرد
        برای جلوگیری از این اتفاق باید یک timespan قرار داده شود.
        در production حتما این کار انجام شود.
        :param request:
        :return:
        """
        user = request.user
        title = request.data.get('title')
        content = request.data.get('content')
        post = Post(user=user, title=title, content=content)
        post.save()
        return Response(data={'id': post.id, 'save': 'Ok'}, status=status.HTTP_201_CREATED)
