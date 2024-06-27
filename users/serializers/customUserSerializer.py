from rest_framework import serializers
import re
from django.core.exceptions import ValidationError
from users.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model= CustomUser
        field = ("id", "name", "email", "password")

    def validate(self, data:dict) -> dict:
        email = data["email"]
        password = data["password"]
        if email: 
            regex = r'^[\w\.\+\-]+\@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            if not re.match(regex, email):
                raise ValidationError('Por favor, insira um endereço de e-mail válido.')
            return email
        regex = r'^(?=.*[0-9])(?=.*[!@#$%^&*()_+\[\]{}|;:',.<>?\/\\]).{1,11}$'
        if not re.match(regex, password):
            raise ValidationError(
                'A senha deve ter no máximo 11 caracteres, incluindo pelo menos um número e um caractere especial.')
        