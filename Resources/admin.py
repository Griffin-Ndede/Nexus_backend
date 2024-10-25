from django.contrib import admin
from .models import Form1Video, Form2Video, Form3Video, Form4Video, Categories

# Register each form-level video model separately
@admin.register(Form1Video)
class Form1VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'video_file', 'cover_image')
    search_fields = ('title',)

@admin.register(Form2Video)
class Form2VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'video_file', 'cover_image')
    search_fields = ('title',)

@admin.register(Form3Video)
class Form3VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'video_file', 'cover_image')
    search_fields = ('title',)

@admin.register(Form4Video)
class Form4VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'video_file', 'cover_image')
    search_fields = ('title',)

# Register the Categories model
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)
