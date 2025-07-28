from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsCurrentAccessTokenForUser # Your custom permission

class MyProtectedDataView(APIView):
    permission_classes = [IsAuthenticated, IsCurrentAccessTokenForUser]

    def get(self, request):
        return Response({"data": "This is highly secret data."})