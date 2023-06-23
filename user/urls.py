from django.urls import path
from .views import (
    UserRegistrationView,
    CustomTokenObtainPairView,
    TokenVerifyView,
    TokenRefreshView,
    UserDetailsView
)

urlpatterns = [
    path("registration/", UserRegistrationView.as_view(), name="user_register"),
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),

    path("<int:pk>/", UserDetailsView.as_view(), name="user_details"),
]
