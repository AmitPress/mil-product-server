from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserSerializer, RegisterSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

@api_view(["POST"])
def login_view(request):
    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.validated_data['user']
        refresh_token = RefreshToken.for_user(user=user)
        access_token = str(refresh_token.access_token)
        refresh_token = str(refresh_token)
        payload = {
            'access_token': access_token,
            'refresh_token': refresh_token
        }
        return Response(data=payload, status=status.HTTP_302_FOUND)
    return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)