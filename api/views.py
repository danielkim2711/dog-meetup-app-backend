from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import get_users_list, create_user, get_user_detail, update_user, delete_user

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'GET': '/users/',
        'POST': '/users/',
        'GET': '/users/<str:pk>/',
        'PUT': '/users/<str:pk>/',
        'DELETE': '/users/<str:pk>/',
    }

    return Response(api_urls)


@api_view(['GET', 'POST'])
def get_users(request):

    if request.method == 'GET':
        return get_users_list(request)

    if request.method == 'POST':
        return create_user(request)


@api_view(['GET', 'PUT', 'DELETE'])
def get_user(request, pk):
    if request.method == 'GET':
        return get_user_detail(request, pk)

    if request.method == 'PUT':
        return update_user(request, pk)

    if request.method == 'DELETE':
        return delete_user(request, pk)
