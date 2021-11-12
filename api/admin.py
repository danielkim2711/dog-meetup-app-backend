from django.contrib import admin
from .models import User, Dog

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'is_administrator')


class DogAdmin(admin.ModelAdmin):
    list_display = ('id', 'dog_name', 'user')


admin.site.register(User, UserAdmin)
admin.site.register(Dog, DogAdmin)
