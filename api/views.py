from django.shortcuts import render
from .models import empoly
from django.contrib.auth.models import User
from .serializers import employModelSerializer,UserModelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from api import serializers

# Create your views here.

class UserViewset(ModelViewSet):
    serializer_class=UserModelSerializer
    queryset=User.objects.all()

class EmployMdelView(ModelViewSet):
    serializer_class=employModelSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    queryset=empoly.objects.all()

    def create(self,request,*args,**kw):
        user=request.user
        ser=employModelSerializer(data=request.data)
        if ser.is_valid():
            ser.save(user=user)
            return Response(data=ser.data,status=status.HTTP_201_CREATED)
        return Response(data=ser.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def destroy(self,request,*args,**kw):
        id=kw.get('pk')
        empoly.objects.filter(id=id).delete()
        return Response(data='item deleted')
    
    def update(self,request,args,*kw):
        eid=kw.get('pk')
        employee=self.queryset.get(id=eid)
        if employee.user==request.user:
            ser=employModelSerializer(employee,data=request.data)
            if ser.is_valid():
             ser.save()
            return Response(data={'msg':'updated'},status=status.HTTP_200_OK)
        else:
            raise serializers.ValidationError("not allowed!")