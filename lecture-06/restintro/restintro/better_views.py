from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView
from .models import User
from .serializer import UserSerializer

class UserListCreateAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'