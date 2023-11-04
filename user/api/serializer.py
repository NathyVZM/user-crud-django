from rest_framework.serializers import ModelSerializer
from ..models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'phone', 'is_staff')
        read_only_fields = ('id',)  # Usar 'read_only_fields' en lugar de 'read_only'