from fish.models import Fish
from fish.serializers import FishSerializer
from rest_framework import viewsets, permissions, authentication
from rest_framework_jwt import authentication as authentication_jwt

# Create your views here.


class FishViewSet(viewsets.ModelViewSet):
    """
    API endpoint to allows fish to be viewed or edited
    """
    queryset = Fish.objects.all()
    serializer_class = FishSerializer

