from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .access_token import generate_access_token
from .utils import timestamp_conversion
from  .encode_base64 import generate_password

def index(request):
    return HttpResponse("sfneo")

class TestView(APIView):

    def get(self, request, format=None):
        access_token = generate_access_token()
        formatted_time = timestamp_conversion()
        decoded_password = generate_password(formatted_time)
        
        return Response({"access_token": access_token, "password ": decoded_password})
    
    