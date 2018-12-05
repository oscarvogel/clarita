from django.contrib import admin

# Register your models here.
from apps.account.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'nacimiento', 'foto']
admin.site.register(Profile, ProfileAdmin)