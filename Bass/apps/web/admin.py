from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from Bass.apps.web.models import Post, Comment, StackComment, Test

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(StackComment)
admin.site.register(Test)