#configures https://buddyguy-api.aswang.co/admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Doctor, Patient

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id','user')
    search_fields = ('user',)

class PatientAdmin(admin.ModelAdmin):
    list_display = ('id','user','doctor')
    search_fields = ('user','doctor')

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active', 'user_type', 'date_joined')
    list_filter = ('email', 'is_staff', 'is_active', 'user_type')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'user_type')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
