from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404
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


class PostList(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    class Meta:
        model = Post
        fields = '__all__'
