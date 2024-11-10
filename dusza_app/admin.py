from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'school','team', 'role','is_staff', 'is_active']  # Add 'extra_field' here
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('school','team','role')}),  # Add 'extra_field' to the form
    )
admin.site.register(User, CustomUserAdmin)
admin.site.register(Team)
admin.site.register(TeamMember)
admin.site.register(School)
admin.site.register(Category)
admin.site.register(ProgLangs)