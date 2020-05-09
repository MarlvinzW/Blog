from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from blog import settings


admin.site.site_header = f"{settings.PLATFORM_NAME} Super Admin"
admin.site.site_title = 'Admin Portal'
admin.site.index_title = f'{settings.PLATFORM_NAME} Admin'


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    list_per_page = 100
    search_fields = ('email', 'username')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info',
         {'fields': ('first_name', 'last_name', 'email', 'picture')
          }),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',),
                         }),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
