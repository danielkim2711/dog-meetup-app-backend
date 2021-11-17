from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import related
from django.db.models.fields.related import OneToOneField

# Create your models here.


class Profile(models.Model):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'

    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
    ]

    picture = models.ImageField(
        null=True, blank=True, upload_to='images/profile/')
    # username = models.CharField(max_length=100, unique=True)
    # password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=100)
    user = models.OneToOneField(User, related_name='user',
                                on_delete=models.CASCADE)
    # is_administrator = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Dog(models.Model):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'

    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
    ]

    picture = models.ImageField(
        null=True, blank=True, upload_to='images/dogs/')
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Activity(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
