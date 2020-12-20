from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from rest_framework import serializers, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from post.models import CustomUser, Post


#
# class UserSerializer(SetCustomErrorMessagesMixin, serializers.ModelSerializer):
#
#     class Meta:
#         model = User
#         fields = ('username', 'password', 'email')
#         custom_error_messages_for_validators = {
#             'username': {
#                 UniqueValidator: _('This username is already taken. Please, try again'),
#                 RegexValidator: _('Invalid username')
#             }
#         }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        # fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}, }
        # exclude=['password',]
        read_only_fields = ('date_joined',)
        # URL_FIELD_NAME='newurl'

    # def create(self, validated_data):


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        exclude = ('password',)


class PostSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = Post
        fields = ('id', 'user', 'title', 'content')
    # username = serializers.CharField(max_length=100)
    # url = serializers.HyperlinkedRelatedField(view_name=CustomUser, queryset=CustomUser.objects.all())
