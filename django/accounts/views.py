from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
from rest_framework.views import APIView
from accounts.serializers import UserRegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken



class RegisterAPIView(APIView):
    serializers_class=UserRegisterSerializer
    def post(self,request,format=None):
        serializer=self.serializers_class(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            refresh=RefreshToken.for_user(user)
            responsedata={
                'refresh':str(refresh),
                'access':str(refresh.access_token),
                'user':str(serializer.data)

            }
            return Response(responsedata,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LogoutAPIView(APIView):
    def post(self,request,format=None):
        
        try:
            refresh_token=request.data['refresh_token']
            tokens_obj = RefreshToken(refresh_token)
            tokens_obj.blacklist()
            return Response("Successful Logout", status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

