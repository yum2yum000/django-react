from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from post.models import CustomUser, Post


@admin.register(CustomUser)
# اگر از کلاس
# UserAdmin
# ارث بری نکند. رمز را هش نمی کند.
class CustomUserAdmin(UserAdmin):
    """
    نحوه ی استفاده از fieldsets
    کل fieldsets یک تاپل می باشد، که هر عضو آن خودن نیز یک تاپل می باشد.
    اعضا به دو بخش تقسیم می شود، بخش اول نام دسته بندی را مشخص می کند و بخش دوم که یک دیکشنری می باشد فیلد ها را مشخص می کند.
    کلید fields در دیکشنری مربوطه یک تاپل که اعضای آن نام فیلدهایی که در قرار است در این دسته بندی وجود داشته باشند نوشته می شود.
    """
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (  # new fieldset added on to the bottom
            'Custom Field Heading',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    #این فیلد جایی هست که خود عکس نمایش داده می شود
                    'avatar_tag',
                    #این فیلد آدرس عکس و انتخاب عکس می باشد.
                    'avatar',

                ),
            },
        ),
        (
            'My fields',
            {
                'fields': ('phone',
                           'desc')
            }
        )
    )
    # list_display = [..., 'image_tag', ]
    readonly_fields = ('avatar_tag',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'send_date']
