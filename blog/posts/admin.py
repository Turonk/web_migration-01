from django.contrib import admin

from .models import Post#, Group

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("pk",  "text")
    search_fields = ("text",)
    empty_value_display = "-пусто-"

'''class GroupAdmin(admin.ModelAdmin):
    list_display=("pk", "title", "description", "slug")
    search_fields = ("title",)
    empty_value_display = "-пусто-"'''

admin.site.register(Post, PostAdmin)
#admin.site.register(Group, GroupAdmin)

