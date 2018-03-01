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

# Use Defualt Permissions and Authentication
    # authentication_classes = (
    #     authentication_jwt.JSONWebTokenAuthentication, authentication.SessionAuthentication)
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


# class FishList(generics.ListCreateAPIView):
#     """
#     API endpoint to allows fish to be viewed or edited
#     """
#     queryset = Fish.objects.all()
#     serializer_class = FishSerializer

# class FishDetail(generics.RetrieveUpdateDestroyAPIView):
#     """
#     API endpoint to allows fish to be viewed or edited
#     """
#     serializer_class = FishSerializer

#     def get_queryset(self):

#         return Fish.objects.all().filter(fishId=self.fishId)
