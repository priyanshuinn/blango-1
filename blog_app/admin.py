from django.contrib import admin
from blog_app.models import Tag, Post
# Register your models here.
admin.site.register(Tag)
#comment
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)