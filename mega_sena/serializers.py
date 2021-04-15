from rest_framework import serializers
from usuario.serializers import UserSerializer
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Game
        fields = ['id', 'numbers', 'date', 'user']
