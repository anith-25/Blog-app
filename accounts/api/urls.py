from django.urls import path
from .views import LoginAPIView, SignupAPIView, LogoutAPIView

urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login_api"),
    path("signup/", SignupAPIView.as_view(), name="signup_api"),
    path("logout/", LogoutAPIView.as_view(), name="logout_api")
]
