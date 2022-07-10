from django.contrib import admin

# Register your models here.
from article.models import Article, Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ['article', 'content']
    list_display_links = ['article'].append(object)
    list_filter = ['article', 'content', 'pubDateTime']
    search_fields = ['content']
    list_editable = ['content']
 
    class Meta:
        model = Comment

admin.site.register(Article)
admin.site.register(Comment)