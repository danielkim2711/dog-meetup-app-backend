from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .utils import create_user, delete_activity, get_user_detail, delete_user, get_profiles_list, create_profile, get_profile_detail, update_profile, delete_profile, get_dogs_list, create_dog, get_dog_detail, update_dog, delete_dog, get_activities_list, create_activity, get_activity_detail, update_activity, delete_activity


# Create your views here.


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'user_username': user.username
        })


# Profiles


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Users': '/users/',
        'Profiles': '/profiles/',
        'Dogs': '/dogs/',
        'Activities': '/activities/',
    }
    return Response(api_urls)


# Users


@api_view(['POST'])
def create_users(request):
    return create_user(request)


@api_view(['GET', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_user(request, pk):
    if request.method == 'GET':
        return get_user_detail(request, pk)

    if request.method == 'DELETE':
        return delete_user(request, pk)


# Profiles


@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def get_profiles(request):
    if request.method == 'GET':
        return get_profiles_list(request)

    if request.method == 'POST':
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


# Activities


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_activities(request):
    if request.method == 'GET':
        return get_activities_list(request)

    if request.method == 'POST':
        return create_activity(request)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_activity(request, pk):
    if request.method == 'GET':
        return get_activity_detail(request, pk)

    if request.method == 'PUT':
        return update_activity(request, pk)

    if request.method == 'DELETE':
        return delete_activity(request, pk)
