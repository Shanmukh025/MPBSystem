from django.contrib import admin
from django.contrib.auth.models import User

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_superuser')


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
