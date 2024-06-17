import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Subs_info
from .serializer import SubsSerializers


class Subs_post(generics.ListCreateAPIView):
    queryset = Subs_info.objects.all()
    serializer_class = SubsSerializers


class Subs_get_post_delete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subs_info.objects.all()
    serializer_class = SubsSerializers


@api_view(["POST"])
def change_password(request):
    # Получаем токен авторизации из заголовка запроса
    auth_header = request.META.get("HTTP_AUTHORIZATION")

    # Проверяем наличие токена авторизации
    if auth_header:
        try:
            # Извлекаем токен из заголовка
            token = auth_header.split(" ")[1]
            # Получаем объект токена из базы данных
            token_obj = Token.objects.get(key=token)
            # Получаем пользователя, связанного с этим токеном
            user = token_obj.user

            # Получаем текущий пароль, новый пароль и подтверждение нового пароля из запроса
            current_password = request.data.get("current_password")
            new_password = request.data.get("new_password")
            confirm_new_password = request.data.get("confirm_new_password")

            # Проверяем, совпадает ли текущий пароль пользователя с введенным паролем
            if not user.check_password(current_password):
                return Response({"error": "Текущий пароль неверен."}, status=status.HTTP_400_BAD_REQUEST)

            # Проверяем, совпадают ли новый пароль и подтверждение нового пароля
            if new_password != confirm_new_password:
                return Response(
                    {"error": "Новый пароль и подтверждение не совпадают."}, status=status.HTTP_400_BAD_REQUEST
                )

            # Устанавливаем новый пароль для пользователя
            user.set_password(new_password)
            user.save()

            return Response({"status": "Password changed successfully"}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            # Если токен не найден, возвращаем ошибку
            return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        # Если токен авторизации не был предоставлен, возвращаем ошибку
        return Response({"error": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)


@method_decorator(csrf_exempt, name="dispatch")
class Register(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")
        username = data.get("username")
        first_name = data.get("first_name")
        last_name = data.get("last_name")

        if User.objects.filter(email=email).exists():
            return JsonResponse({"status": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)
        token = Token.objects.create(user=user)

        user = authenticate(request, username=user.username, password=password)
        login(request, user)  # при регистрации сразу же заходим в аккаунт

        return JsonResponse({"status": "User created", "token": token.key}, status=status.HTTP_201_CREATED)


@method_decorator(csrf_exempt, name="dispatch")
class Login(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")

        # Проверяем, существует ли пользователь с таким email
        user = User.objects.filter(email=email).first()

        # Если пользователь существует и пароль верен, аутентифицируем его
        if user is not None and user.check_password(password):
            user = authenticate(request, username=user.username, password=password)

            if user is not None:
                login(request, user)
                token, _ = Token.objects.get_or_create(user=user)
                return JsonResponse({"status": "Logged in", "token": token.key}, status=status.HTTP_200_OK)

        return JsonResponse({"status": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name="dispatch")
class Logout(View):
    def post(self, request):
        logout(request)
        return JsonResponse({"status": "Logged out"}, status=status.HTTP_200_OK)


class Profile(View):
    def get(self, request):
        if "HTTP_AUTHORIZATION" in request.META:
            auth_header = request.META["HTTP_AUTHORIZATION"]
            token = auth_header.split(" ")[1]  # Получаем токен из заголовка авторизации

            try:
                user = Token.objects.get(key=token).user
                return JsonResponse({"username": user.username, "email": user.email, "first_name":user.first_name, "last_name":user.last_name}, status=status.HTTP_200_OK)
            except Token.DoesNotExist:
                return JsonResponse({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)

        return JsonResponse(
            {"error": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED
        )
