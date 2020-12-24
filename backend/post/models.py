import re
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.html import format_html


class LowercaseEmailField(models.EmailField):
    def to_python(self, value):
        value = super().to_python(value)
        if isinstance(value, str):
            return value.lower()
        return value


class CustomUser(AbstractUser):
    class Meta:
        pass

    # قابل نال کردن فیلد نام
    # AbstractUser._meta.get_field('first_name)._unique=False
    AbstractUser._meta.get_field('first_name').null = True
    AbstractUser._meta.get_field('last_name').null = True
    email = LowercaseEmailField(null=True, unique=False, default=None, blank=True, )
    phone = models.CharField('شماره تلفن', max_length=11, null=True,
                             blank=True, )
    adres = models.TextField('آدرس', null=True, blank=True)
    bio = models.TextField('توضیحات', null=True, blank=True)
    avatar = models.ImageField('تصویر', upload_to='images', null=True, blank=True)

    def clean(self):
        # phone validate
        if self.phone is not None and re.match('^09[0-9]{9}$', self.phone) is None:
            raise ValidationError('phone format is invalid')

        # email validate
        user = ''
        try:
            user = CustomUser.objects.get(email=self.email)
            # اگر ایمیل وارد شده در دیتابیس وجود داشته باشد
        except:
            pass
        if user:
            raise ValidationError('Email is duplicate')

    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['password']

    def __str__(self):
        return f'{self.username}'

    # این متد برای نشان دادن عکس در پنل ادمین است.
    # برای کارکرد درست این متد، باید تغییراتی در فایل admin
    # داده شود
    # به فایل admin مراجعه شود
    def avatar_tag(self):
        # تابع format_html و mark_safe ورودی را به یک فایل html می چسبانند
        return format_html('<img src="%s" width="150px" height="150px" />' % (self.avatar.url))

    avatar_tag.short_description = 'تصویر'


class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_DEFAULT, default='deleted')
    title = models.CharField('عنوان', max_length=100, null=False)
    content = models.TextField('محتوا', null=False)
    send_date = models.DateTimeField('تاریخ ارسال', auto_now_add=True)
    last_update = models.DateTimeField('تاریخ آخرین اپدیت', auto_now=True)

    class Meta:
        unique_together = ('user', 'title')

    def __str__(self):
        return f'{self.title}-{self.user.username}'
