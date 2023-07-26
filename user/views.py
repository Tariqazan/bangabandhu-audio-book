from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from .models import User
from .serializers import UserSerializer, UserRegistrationSerializer


class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        # Call the parent's post method to get the token pair
        response = super().post(request, *args, **kwargs)

        # Perform any additional customizations or checks here
        # ...

        # Return the customized response
        return Response(response.data, status=response.status_code)


class TokenVerifyView(APIView):
    def post(self, request):
        token = request.data.get("token")

        try:
            # Verify the token
            access_token = AccessToken(token)
            # Access the claims of the token
            user_id = access_token["user_id"]
            # Additional checks or operations with the token
            # ...
            return Response({"valid": True})
        except Exception:
            return Response({"valid": False})


class TokenRefreshView(APIView):
    def post(self, request):
        token = request.data.get("token")

        try:
            # Create a RefreshToken instance
            refresh_token = RefreshToken(token)
            # Refresh the token
            access_token = refresh_token.access_token
            # Additional checks or operations with the refreshed token
            # ...
            return Response({"access_token": str(access_token)})
        except Exception:
            return Response(status=400)


class UserDetailsView(APIView):
    queryset = User
    serializer_class = UserSerializer

    def get_object(self):
        id = self.request.user.id
        user = self.queryset.objects.get(id=id)
        return user

    def get(self, *args, **kwargs):
        user = self.get_object()
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.serializer_class(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        refresh_token = request.data.get("refresh_token")

        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response({"message": "Logout successful."})
            except Exception:
                return Response({"message": "Invalid refresh token."}, status=400)
        else:
            return Response({"message": "Refresh token not provided."}, status=400)


class DashboardView(APIView):
    def get(self, request, *args, **kwargs):
        total_users = User.objects.all().count()
        response = {
            "total_users": total_users
        }
        return Response(response)
