from django.shortcuts import render
from django.contrib.auth.models import User
import rest_framework
import rest_framework.generics
import rest_framework.permissions
from .serializers import UserSerializer, NoteSerializer
from .models import Note

class NoteListCreate(rest_framework.generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [rest_framework.permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(rest_framework.generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [rest_framework.permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    


# Create your views here.
class CreateUserView(rest_framework.generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [rest_framework.permissions.AllowAny]
