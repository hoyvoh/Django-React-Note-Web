from django.contrib.auth.models import User
import rest_framework
import rest_framework.serializers
from .models import Note

class UserSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password":{"write_only":True}}

    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        return user
    
class NoteSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'author']
        extra_kwargs = {"author":{"read_only":True}}
    
