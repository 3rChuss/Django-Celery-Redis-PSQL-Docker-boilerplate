from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import permissions, status

from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

# Create with APIView
class HelloWorld(APIView):
    serializer_class = None
    def get(self, request):
        return Response({"message": "Hello, world!"})
    

# Create with CreateAPIView
from rest_framework.generics import CreateAPIView

class CreateUser(CreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = None

    def post(self, request):
        return Response({"message": "User created!"})


class CachedTestView(APIView):
    @method_decorator(cache_page(60))

    def get(self, request):
        user_model = get_user_model()
        all_users = user_model.objects.all()
        return Response({"message": "Cache test view", "users": all_users})
    

class CacheLessTestView(APIView):
    def get(self, request):
        user_model = get_user_model()
        all_users = user_model.objects.all()
        return Response({"message": "CacheLess test view", "users": all_users})