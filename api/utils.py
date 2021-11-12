from rest_framework.response import Response
from .models import User, Dog
from .serializers import UserSerializer, DogSerializer


def get_users_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


def get_user_detail(reqeust, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


def create_user(request):
    data = request.data
    serializer = UserSerializer(data, many=False)
    return Response(serializer.data)


def update_user(request, pk):
    data = request.data
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=data)

    if serializer.is_valid():
        serializer.save()

    return serializer.data


def delete_user(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return Response('User successfully deleted!')
