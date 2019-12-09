from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

def index(request):
    return HttpResponse(request, "Device API")

class DevieAPIView(APIView):
    serializer_class = serializers.DeviceSerializer

    def get(self, request, format=None):
        apis_supported = [
            'HEAD',
            'OPTIONS',
            'GET',
            'POST',
            'PUT',
            'PATCH',
            'DELETE',
        ]
        return Response({'message':'The list of HTTP methods suported',
                         'apis_supported':apis_supported})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Device Name: {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({'message':"PUT success"})

    def patch(self, request, pk=None):
        return Response({'message':'PATCH Successful'})

    def delete(self, request, pk=None):
        return Response({'message':'DELETE success'})

