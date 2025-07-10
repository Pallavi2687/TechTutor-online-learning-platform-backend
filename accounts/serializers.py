import re
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


# ──────────────────────────  Register  ──────────────────────────
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model  = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    # 1. username: letters only + unique
    def validate_username(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Username must contain letters only.")
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken.")
        return value

    # 2. password: 8‑15 chars, at least 1 letter and 1 number
    def validate_password(self, value):
        if not 8 <= len(value) <= 15:
            raise serializers.ValidationError("Password must be 8–15 characters long.")
        if not (re.search(r"[A-Za-z]", value) and re.search(r"\d", value)):
            raise serializers.ValidationError("Password must include letters and numbers.")
        return value

    # 3. create user
    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )


# ──────────────────────────  JWT with extra claims  ──────────────
class CustomTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['is_staff']  = user.is_staff
        token['username']  = user.username
        return token
