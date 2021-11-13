from django.db import models

# Create your models here.


class User(models.Model):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'

    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
    ]

    user_name = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    is_administrator = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Dog(models.Model):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'

    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
    ]

    dog_name = models.CharField(max_length=100)
    dog_breed = models.CharField(max_length=100)
    dog_gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.dog_name
