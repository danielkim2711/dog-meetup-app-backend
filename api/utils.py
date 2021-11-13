from rest_framework import status
from rest_framework.response import Response
from .models import User, Dog
from .serializers import UserSerializer, DogSerializer


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


def get_user_detail(reqeust, pk):
    try:
        user = User.objects.get(pk=pk)

    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


def update_user(request, pk):
    try:
        user = User.objects.get(pk=pk)

    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


def delete_user(request, pk):
    try:
        user = User.objects.get(pk=pk)

    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
