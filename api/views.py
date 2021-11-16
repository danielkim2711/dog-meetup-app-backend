from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .utils import create_user, create_profile, get_profile_detail, update_profile, delete_profile, get_dogs_list, create_dog, get_dog_detail, update_dog, delete_dog

# Create your views here.

# Profiles


@api_view(['GET'])
def apiOverview(request):
    api_urls = [
        {
            'Endpoint': 'profiles/',
            'method': 'GET',
            'body': None,
            'description': 'Return an array of profiles'
        },
        {
            'Endpoint': 'profiles/',
            'method': 'POST',
            'body': {
                # 'user_name': '',
                # 'password': '',
                'picture',
                'first_name',
                'last_name',
                'gender',
                'email',
                'address',
            },
            'description': 'Create new profile with data sent in POST request'
        },
        {
            'Endpoint': 'profiles/<int:pk>/',
            'method': 'GET',
            'body': None,
            'description': 'Return a single profile object'
        },
        {
            'Endpoint': 'profiles/<int:pk>/',
            'method': 'PUT',
            'body': {
                # 'user_name',
                # 'password',
                'picture',
                'first_name',
                'last_name',
                'gender',
                'email',
                'address',
            },
            'description': 'Update an existing profile with data sent in PUT request'
        },
        {
            'Endpoint': 'profiles/<int:pk>/',
            'method': 'DELETE',
            'body': None,
            'description': 'Delete an existing profile'
        },
    ]
    return Response(api_urls)


# Users


@api_view(['POST'])
def create_users(request):
    return create_user(request)


# Profiles


# @api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def get_profiles(request):
#     return get_profiles_list(request)


@api_view(['POST'])
def create_profiles(request):
    return create_profile(request)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_profile(request, pk):
    if request.method == 'GET':
        return get_profile_detail(request, pk)

    if request.method == 'PUT':
        return update_profile(request, pk)

    if request.method == 'DELETE':
        return delete_profile(request, pk)


# Dogs


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_dogs(request):
    if request.method == 'GET':
        return get_dogs_list(request)

    if request.method == 'POST':
        return create_dog(request)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_dog(request, pk):
    if request.method == 'GET':
        return get_dog_detail(request, pk)

    if request.method == 'PUT':
        return update_dog(request, pk)

    if request.method == 'DELETE':
        return delete_dog(request, pk)
