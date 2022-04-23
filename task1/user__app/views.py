from django.shortcuts import render
from user__app.serializer import user_serializers, customer_serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['POST'])
def userdata(request, format=None):

    if request.method == 'POST':
        serializer = user_serializers(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])

def customerdata(request, format=None):

    if request.method == 'POST':
        serializer = customer_serializers(data= request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

