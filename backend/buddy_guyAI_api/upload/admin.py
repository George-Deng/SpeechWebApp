from django.contrib import admin

from .models import Upload


class UploadAdmin(admin.ModelAdmin):
    list_display = ('id','uploaded_at','file', 'patient')

admin.site.register(Upload)
# @admin.site.register(UploadPrivate)
# class UploadAdmin(admin.ModelAdmin):
#     list_display = ('id','uploaded_at','file')
