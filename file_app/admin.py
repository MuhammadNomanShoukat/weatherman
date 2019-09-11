from django.contrib import admin
from .models import FileData

# ======================================== FileAdmin class inheriting ModelAdmin to customize the admin panel ===========
class FileAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'file_name',
    ]
    list_filter = [
        # 'file_name',
        'max_temp',
        'min_temp',
        'max_humd',
        'min_humd',
        'mean_humd',
    ]

""" FileData registring on admin site"""
admin.site.register(FileData,FileAdmin)
