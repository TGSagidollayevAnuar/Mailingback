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

class MailSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField()
    text = serializers.CharField()
    author = UserSerializer()
    receiver = UserSerializer()

class DraftSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField()
    text = serializers.CharField()
    author = UserSerializer()    

