from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Team)
admin.site.register(TeamMember)
admin.site.register(School)
admin.site.register(Category)
admin.site.register(ProgLangs)