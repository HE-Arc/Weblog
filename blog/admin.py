from django.contrib import admin
from .models import Article, Category, Tag


# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    # fields = ('title', 'body', 'view_cat_name', 'tags', 'slug')
    fields = ('title', 'body', 'tags', 'slug', 'author')

    # def view_cat_name(self, obj):
    #     return obj.name


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']


class TagAdmin(admin.ModelAdmin):
    fields = ['name']


class UserAdmin(admin.ModelAdmin):
    fields = ['name']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)