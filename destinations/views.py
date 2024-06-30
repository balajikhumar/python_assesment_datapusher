from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import Account
from .models import Destination
from .serializers import DestinationSerializer
import requests

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    
    
    
class IncomingDataView(APIView):

    def post(self, request):
        token = request.headers.get('CL-X-TOKEN')
        if not token:
            return Response({"message": "Un Authenticate"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            account = Account.objects.get(app_secret_token=token)
        except Account.DoesNotExist:
            return Response({"message": "Un Authenticate"}, status=status.HTTP_401_UNAUTHORIZED)

        for destination in account.destinations.all():
            headers = destination.headers
            method = destination.http_method
            url = destination.url

            if method == 'GET':
                response = requests.get(url, params=request.data, headers=headers)
            elif method == 'POST':
                response = requests.post(url, json=request.data, headers=headers)
            elif method == 'PUT':
                response = requests.put(url, json=request.data, headers=headers)

        return Response({"message": "Data Sent"}, status=status.HTTP_200_OK)
