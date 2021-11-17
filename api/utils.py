from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Profile, Dog
from .serializers import UserSerializer, ProfileSerializer, DogSerializer


# Users

def get_users_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


def create_user(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Profiles


def get_profiles_list(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)


def create_profile(request):
    serializer = ProfileSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_profile_detail(reqeust, pk):
    try:
        profile = Profile.objects.get(pk=pk)

    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)


def update_profile(request, pk):
    try:
        profile = Profile.objects.get(pk=pk)

    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProfileSerializer(profile, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


def delete_profile(request, pk):
    try:
        profile = Profile.objects.get(pk=pk)

    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    profile.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# Dogs


def get_dogs_list(request):
    dogs = Dog.objects.all()
    serializer = DogSerializer(dogs, many=True)
    return Response(serializer.data)


def create_dog(request):
    serializer = DogSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_dog_detail(reqeust, pk):
    try:
        dog = Dog.objects.get(pk=pk)

    except Dog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = DogSerializer(dog, many=False)
    return Response(serializer.data)


def update_dog(request, pk):
    try:
        dog = Dog.objects.get(pk=pk)

    except Dog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = DogSerializer(dog, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


def delete_dog(request, pk):
    try:
        dog = Dog.objects.get(pk=pk)

    except Dog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    dog.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
