from rest_framework import serializers

from post.models import CustomUser, Post


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        # fields = ('username', 'first_name', 'last_name')
        fields = '__all__'
        read_only_fields = ('email',)
        # URL_FIELD_NAME='newurl'
    # username = serializers.CharField(max_length=100)
    # def get_permissions(self):


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        exclude = ('password',)


class PostSerializer(serializers.HyperlinkedModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = Post
        fields = ('user', 'title', 'content')
    # username = serializers.CharField(max_length=100)
    # url = serializers.HyperlinkedRelatedField(view_name=CustomUser, queryset=CustomUser.objects.all())
