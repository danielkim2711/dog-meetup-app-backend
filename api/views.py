from django.shortcuts import render

from rest_framework.response import Response

# Create your views here.


def test(request):
    return Response('Hello World')
