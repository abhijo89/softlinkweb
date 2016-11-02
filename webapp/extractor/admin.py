from django.contrib import admin

from .models import *

class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')


class AdminArticle(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')

class AdminAuthor(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')

class AdminTag(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')

class AdminNewsPaper(admin.ModelAdmin):
    list_display = ('url', 'chanel', 'name', 'is_enable', 'created', 'updated')

admin.site.register(NewsPaper, AdminNewsPaper)
admin.site.register(Author, AdminAuthor)
admin.site.register(Article, AdminArticle)
admin.site.register(Tag, AdminTag)
admin.site.register(Image)
admin.site.register(Video)
admin.site.register(NewsChanel)
admin.site.register(Category, AdminCategory)
