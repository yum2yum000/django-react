from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class CustomUser(AbstractUser):
    class Meta:
        pass

    phone = models.CharField('شماره تلفن', max_length=11, null=True, blank=True)
    adres = models.TextField('آدرس', null=True, blank=True)
    desc = models.TextField('توضیحات', null=True, blank=True)
    avatar = models.ImageField('تصویر', upload_to='images', null=True, blank=True)

    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['password']

    def __str__(self):
        return f'{self.username}'

