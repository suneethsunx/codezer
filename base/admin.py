from django.contrib import admin

from .models import *


# Code files
class CodeFileAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at']
admin.site.register(CodeFile, CodeFileAdmin)
