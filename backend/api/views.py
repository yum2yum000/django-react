from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404, CreateAPIView
from rest_framework.response import Response
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

class UserViewSets(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


# class PostList(ListAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#
#     class Meta:
#         model = Post
#         fields = '__all__'


class CreateUser(CreateAPIView):
    serializer_class = UserSerializer
    #
    # def get(self, request):
    #     if request.method.POST:
    #         username = request.POST['username']
    #         password = request.POST['password']
    #         data = UserViewSets((username, password)).data
    #         return Response(data)




class PostList(APIView):
    def get(self, request):
        objs = Post.objects.all()
        data = PostSerializer(objs, many=True).data
        return Response(data)


class PostDetail(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(Post, pk=pk)
        data = PostSerializer(obj, many=False).data
        return Response(data)
