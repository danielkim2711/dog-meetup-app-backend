from django.contrib import admin
from .models import User, Dog

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')


class DogAdmin(admin.ModelAdmin):
    list_display = ('id', 'dog_name')


admin.site.register(User, UserAdmin)
admin.site.register(Dog, DogAdmin)
