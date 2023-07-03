from django.shortcuts import render
from django.http import Http404, HttpResponseBadRequest, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from container.serializers import *
from container.models import *
from container.permissions import IsOwner
from django.db.models import Q 


class checklistapi(APIView):
    permission_classes=[IsAuthenticated,IsOwner]
    serializers_class=ReceipeItemSerializer
    def get(self,request,format=None):
        category_choice = request.query_params.get('category', None)
        if category_choice:
            try:
                data = Receipe.objects.filter(Q(category_id=category_choice) & ~Q(receipe_user_id=request.user))
                print(data)
            except:
                error_response = {'error': 'Invalid category'}
                return JsonResponse(error_response, status=400)
        else:
            data=Receipe.objects.filter(~Q(receipe_user_id=request.user))
        
        serializer=self.serializers_class(data,many=True)
        seralized_data=serializer.data
        return Response(seralized_data,status=status.HTTP_200_OK)


class categorylist(APIView):
    permission_classes=[IsAuthenticated,IsOwner]
    serializers_class=categorylistSerializer
    def get(self,request,format=None):
        
        data=ReceipeCategory.objects.all()

        serializer=self.serializers_class(data,many=True)
        seralized_data=serializer.data
        return Response(seralized_data,status=status.HTTP_200_OK)
    
class CategoryListDetail(APIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = ReceipeSerializer

    def get(self, request, uuid_check, format=None):
        data = Receipe.objects.filter(receipe_id=uuid_check)
        serializer = self.serializer_class(data, many=True)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)
