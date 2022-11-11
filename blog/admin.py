from typing import Optional, Sequence
from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    
    list_filter = ['status', 'created', 'publish', 'author']
    
    search_fields: Sequence[str] = ['title', 'body']
    
    prepopulated_fields= {'slug': ('title',)}
    
    raw_id_fields: Sequence[str] = ['author']
    
    date_hierarchy: Optional[str] = 'publish'
    
    ordering = ['status', 'publish']
