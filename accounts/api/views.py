from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model
from .serializers import SignupSerializer
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token = Token.objects.create(user=user)
            return Response({"token": token.key})
        else:
            raise AuthenticationFailed
        

class SignupAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user:
            token = Token.objects.create(user=user)
            return Response({"token": token.key})
        else:
            raise AuthenticationFailed
        

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        token_header = request.META.get('HTTP_AUTHORIZATION')
        token = token_header.replace("Token ", "").strip()
        Token.objects.filter(key=token).delete()
        return Response({"message": "Successfully Logged out."})