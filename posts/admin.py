from django.contrib import admin
from .models import CustomUser, Post

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'contact_number', 'is_active']
    list_filter = ['is_active']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at']
