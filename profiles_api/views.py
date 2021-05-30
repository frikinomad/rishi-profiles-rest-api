from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    """Test API View"""
    def get(self, request, format=None):
        """Returns a list of API views feature"""
        an_apiview = [
            'uses HTTP methods as function',
            'get, put, patch, etc, similar to traditional django view',
        ]
    
        return Response({'message': 'hello', 'an_apiview': an_apiview}) 