from rest_framework import serializers
from api.models import User, Manager

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'name'

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = 'id', 'username'

