from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from post.models import CustomUser


@admin.register(CustomUser)
# اگر از کلاس
# UserAdmin
# ارث بری نکند. رمز را هش نمی کند.
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (  # new fieldset added on to the bottom
            'Custom Field Heading',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
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
