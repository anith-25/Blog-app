from rest_framework import serializers
from django.contrib.auth import get_user_model
from .exceptions import MailAlreadyInUseException, PasswordsDoNotMatchException

User = get_user_model()

class SignupSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")
        if username and password:
            if User.objects.filter(username__iexact=username).exists():
                raise MailAlreadyInUseException
            elif not password == confirm_password:
                raise PasswordsDoNotMatchException
        return attrs

    def create(self, validated_data):
        username = validated_data.get("username")
        password = validated_data.get("password")
        user = User.objects.create(
            username=username,
        )
        user.set_password(password)
        user.save()
        return user