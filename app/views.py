from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .serializer import UserSerializer
from django.contrib.auth.hashers import make_password, check_password


#Receber email e senha, transformar a senha em um hash, colocar em um dicionário, guardar a senha e o email no banco de dados.

@csrf_exempt
@api_view(['POST'])
def user(request):
    if request.method == 'POST':
        request.data['password']
        hashed_password = make_password(request.data['password'])
        data = {'email':request.data['email'], 'password':hashed_password}
        print(data)

        serializer = UserSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)