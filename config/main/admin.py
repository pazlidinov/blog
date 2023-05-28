from django.contrib import admin
from django.utils.html import mark_safe
from .models import Category, Article, Tag, Comment, Reply_Comment
# Register your models here.

admin.site.register(Comment)
admin.site.register(Reply_Comment)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['image_tag', 'title', 'category', 'author', 'published']
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ["title"]
    list_per_page = 10
    readonly_fields = ['image_tag']

    def image_tag(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
