from django.contrib import admin
from .models import blog_article,author

class article_admin(admin.ModelAdmin):
    list_display = ('title','slug','created_on','status')
    list_filter = ("status",)
    search_fields = ['title','content']
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(blog_article,article_admin)
admin.site.register(author)
