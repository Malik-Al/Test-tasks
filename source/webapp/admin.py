from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from webapp.models import Profile, Token


class ProfileInline(admin.StackedInline):
    model = Profile
    fields = ['second_name', 'avatar', 'gender', 'country']


class ProfileAdmin(UserAdmin):
    inlines = [ProfileInline]


admin.site.register(Token)
admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)


