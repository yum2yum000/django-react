from django.contrib.auth import authenticate
from rest_framework import viewsets, status
from rest_framework import generics
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

    def put(self, request, id):
        # توکن ارسالی مربوط به ای دی ارسالی می باشد و این کاربر مجاز به تغییرات در پروفایل است
        if str(request.user.id) == id:
            user = CustomUser.objects.get(id=id)
            user.phone = request.data.get('phone')
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class LoginView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({'token': user.auth_token.key})
        else:
            return Response({'error': 'Wrong Credentials'}, status=status.HTTP_400_BAD_REQUEST)


#
class PostList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        # زمانی که این متد فراخوانی شود یعنی توکن تایید شده است و
        # request.user
        # در دسترس قرار می گیرد.
        user_id = request.user.id
        # ایدی ارسالی مربوط به ایدی صاحب توکن است یا خیر
        # در صورتی که توکن تایید شود
        # request.user
        # در دسترس قرار میگیرد
        if str(user_id) == id:
            objs = Post.objects.filter(user_id=user_id)
            data = PostSerializer(objs, many=True).data
            return Response(data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class PostDetail(APIView):
    def get(self, request, pk):
        obj = generics.get_object_or_404(Post, pk=pk)
        data = PostSerializer(obj, many=False).data
        return Response(data)
