from django.contrib import admin
from .models import Profile, Dog, Activity

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')


class DogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'profile')


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('profile', 'title', 'created')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Dog, DogAdmin)
admin.site.register(Activity, ActivityAdmin)
