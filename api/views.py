from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import get_users_list, create_user, get_user_detail, update_user, delete_user

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = [
        {
            'Endpoint': 'users/',
            'method': 'GET',
            'body': None,
            'description': 'Return an array of users'
        },
        {
            'Endpoint': 'users/',
            'method': 'POST',
            'body': {
                'user_name': '',
                'first_name': '',
                'last_name': '',
                'gender': '',
                'email': '',
                'password': '',
                'address': '',
            },
            'description': 'Create new user with data sent in POST request'
        },
        {
            'Endpoint': 'users/<int:pk>/',
            'method': 'GET',
            'body': None,
            'description': 'Return a single user object'
        },
        {
            'Endpoint': 'users/<int:pk>/',
            'method': 'PUT',
            'body': {
                'user_name': '',
                'first_name': '',
                'last_name': '',
                'gender': '',
                'email': '',
                'password': '',
                'address': '',
            },
            'description': 'Update an existing user with data sent in PUT request'
        },
        {
            'Endpoint': 'users/<int:pk>/',
            'method': 'DELETE',
            'body': None,
            'description': 'Delete an existing user'
        },
    ]
    return Response(api_urls)


@ api_view(['GET', 'POST'])
def get_users(request):
    if request.method == 'GET':
        return get_users_list(request)

    if request.method == 'POST':
        return create_user(request)


@ api_view(['GET', 'PUT', 'DELETE'])
def get_user(request, pk):
    if request.method == 'GET':
        return get_user_detail(request, pk)

    if request.method == 'PUT':
        return update_user(request, pk)

    if request.method == 'DELETE':
        return delete_user(request, pk)
