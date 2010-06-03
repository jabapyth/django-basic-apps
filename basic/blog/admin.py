from django.contrib import admin
from basic.blog.models import *

try:
    from reversion.admin import VersionAdmin
    Admin = VersionAdmin
except ImportError:
    Admin = admin.ModelAdmin

class CategoryAdmin(Admin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Category, CategoryAdmin)

class PostAdmin(Admin):
    list_display  = ('title', 'publish', 'status')
    list_filter   = ('publish', 'categories', 'status')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Post, PostAdmin)


class BlogRollAdmin(Admin):
    list_display = ('name', 'url', 'sort_order',)
    list_editable = ('sort_order',)
admin.site.register(BlogRoll)

admin.site.register(Image)
