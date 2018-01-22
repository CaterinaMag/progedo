from django.contrib import admin
from blog import models


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']} # mi calcola il campo slug in automatico


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']} # come sopra

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Category, CategoryAdmin) # esite la tabella delle categorie
admin.site.register(models.Post, PostAdmin) # esiste la tabella dei post
admin.site.register(models.Comment, CommentAdmin)
