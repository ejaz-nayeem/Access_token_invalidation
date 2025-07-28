from django.shortcuts import render

# Create your views here.
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomUserTokenObtainPairSerializer
# ... your other imports

class CustomUserLoginView(TokenObtainPairView):
    """
    The login endpoint that uses our custom serializer to enforce
    a single active session by updating the JTI on the user model.
    """
    serializer_class = CustomUserTokenObtainPairSerializer

# ... your other views like MyProtectedDataView ...