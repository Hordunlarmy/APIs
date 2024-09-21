from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User


class SignUpSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["url", "username", "email", "password"]

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class SignInSerializer(SignUpSerializer):
    class Meta(SignUpSerializer.Meta):
        fields = ["username", "password"]

    def validate(self, data):
        user = authenticate(
            username=data.get("username"), password=data.get("password")
        )
        if not user:
            raise serializers.ValidationError("Invalid username or password.")
        data["user"] = user
        return data
