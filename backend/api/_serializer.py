from django.contrib.auth import password_validation
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from post.models import CustomUser, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'phone')
        # fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
        # exclude=['password',]
        # read_only_fields = ('email',)
        # URL_FIELD_NAME='newurl'

    def validate(self, data):
        password_validation.validate_password(data.get('password'))
        return data



    def create(self, validated_data):
        user = CustomUser(
            username=validated_data.get('username'),
            phone=validated_data.get('phone'),
            # email=validated_data ...
        )
        user.set_password(validated_data.get('password'))
        user.save()
        Token.objects.create(user=user)
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
        fields = ('id','user', 'title', 'content')
    # username = serializers.CharField(max_length=100)
    # url = serializers.HyperlinkedRelatedField(view_name=CustomUser, queryset=CustomUser.objects.all())
