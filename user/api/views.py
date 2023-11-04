from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from ..models import User
from .serializer import UserSerializer

class UserApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = UserSerializer(User.objects.all(), many=True)
        return Response(users.data, status=status.HTTP_200_OK)

    def post(self, request):
        user = UserSerializer(data=request.data)
        user.is_valid(raise_exception=True)
        user.save()
        return Response(user.data, status=status.HTTP_201_CREATED)

class UserViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        users = UserSerializer(User.objects.all(), many=True)
        return Response(users.data, status=status.HTTP_200_OK)

    def create(self, request):
        user = UserSerializer(data=request.data)
        user.is_valid(raise_exception=True)
        user.save()
        return Response(user.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        user = UserSerializer(User.objects.get(pk=pk))
        return Response(user.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user = UserSerializer(User.objects.get(pk=pk), data=request.data)
        user.is_valid(raise_exception=True)
        user.save()
        return Response(user.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def login(self, request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'message': 'Logged in successfully'})
            else:
                return JsonResponse({'message': 'Invalid login credentials'})
        return JsonResponse({'message': 'Please use a POST request to log in'})



class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []