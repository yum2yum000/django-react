from rest_framework import serializers

from post.models import CustomUser, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        # fields = ('username', 'first_name', 'last_name')
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
        # exclude=['password',]
        # read_only_fields = ('email',)
        # URL_FIELD_NAME='newurl'

    # username = serializers.CharField(max_length=100)
    # def get_permissions(self):
    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            # email=validated_data
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        exclude = ('password',)


class PostSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = Post
        fields = ('user', 'title', 'content')
    # username = serializers.CharField(max_length=100)
    # url = serializers.HyperlinkedRelatedField(view_name=CustomUser, queryset=CustomUser.objects.all())
