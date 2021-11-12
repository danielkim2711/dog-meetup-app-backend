from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=100)


class Dog(models.Model):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'

    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
    ]

    dog_name = models.CharField(max_length=100)
    dog_breed = models.CharField(max_length=100)
    dog_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
