from django.contrib import admin
from .models import User, Dog, Event

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'is_administrator')


class DogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')


class EventAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created')


admin.site.register(User, UserAdmin)
admin.site.register(Dog, DogAdmin)
admin.site.register(Event, EventAdmin)
