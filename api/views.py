# views.py
from rest_framework import generics
from rest_framework.response import Response
from .models import UserEmail
from .serializers import UserEmailSerializer

class UserEmailCreateView(generics.CreateAPIView):
    queryset = UserEmail.objects.all()
    serializer_class = UserEmailSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UsersV(generics.ListAPIView):
    queryset = UserEmail.objects.all()
    serializer_class = UserEmailSerializer
