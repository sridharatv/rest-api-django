from rest_framework.views import APIView
from rest_framework.response import Response

class DevieAPIView(APIView):

    def get(self, request, format=None):
        apis_supported = [
            'GET',
            'POST',
            'PUT',
            'DELETE',
            'UPDATE',
            'PATCH',
        ]
        return Response({'message':'The list of HTTP methods suported',
                         'apis_supported':apis_supported})

