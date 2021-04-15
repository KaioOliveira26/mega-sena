from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .serializers import UserSerializer
from .services import validate_token_user


class UserCreateView(APIView):
    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, 400)

        user = User.objects.create_user(**request.data)

        serializer = UserSerializer(user)

        return Response(serializer.data, 201)


class UserView(APIView):
    def get(self, request):
        return Response(UserSerializer(User.objects.filter(is_active=True), many=True).data)

    def patch(self, request):
        valid = validate_token_user(request.headers)

        if valid['response'] != True:
            return Response({'response': valid['response']}, valid['status'])

        if "password" in request.data:
            request.data['password'] = make_password(request.data['password'])
        user_object = valid['user']
        serializer = UserSerializer(
            user_object, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response("wrong parameters", 400)

    def delete(self, request):
        valid = validate_token_user(request.headers)

        if valid['response'] != True:
            return Response({'response': valid['response']}, valid['status'])

        user_object = valid['user']
        user_object.is_active = False
        user_object.save()
        return Response(status=204)
