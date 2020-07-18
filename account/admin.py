from django.contrib import admin

# Register your models here.
from .models import UserProfile

class UserprofileAdmin(admin.ModelAdmin) : 
    list_display = ('id', 'user', 'profile_image', 'summary')
    list_display_links = ('id', 'user')

admin.site.register(UserProfile, UserprofileAdmin)