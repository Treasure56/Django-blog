from django.contrib import admin
from . models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'popular', 'reporter', 'blog_date')
    list_display_links = ('title', 'reporter')
    list_filter = ('reporter',)
    search_fields = ('title',)
    list_per_page = 25
    
admin.site.register(BlogPost, BlogPostAdmin)


