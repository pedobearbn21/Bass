from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
# from django.utils.html import format_html

from Bass.apps.web.models import Payment,Post, Comment, WareHouse, Test

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(WareHouse)
admin.site.register(Test)
admin.site.register(Payment)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)