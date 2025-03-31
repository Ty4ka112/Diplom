# Импортируем модуль serializers из rest_framework для создания сериализаторов
from rest_framework import serializers
# Импортируем модель User из django.contrib.auth.models для работы с пользователями
from django.contrib.auth.models import User
# Импортируем модели Task, Category и Priority из текущего модуля models
from .models import Task, Category, Priority

# Определяем сериализатор для модели User
class UserSerializer(serializers.ModelSerializer):
    # Внутренний класс Meta для указания метаданных
    class Meta:
        # Указываем модель, которую будем сериализовать
        model = User
        # Задаем поля, которые будут включены в сериализацию
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

# Определяем сериализатор для модели Task
class TaskSerializer(serializers.ModelSerializer):
    # Внутренний класс Meta для указания метаданных
    class Meta:
        # Указываем модель, которую будем сериализовать
        model = Task
        # Задаем поля, которые будут включены в сериализацию
        fields = ['id', 'title', 'description', 'status', 'category', 'priority', 'created_by', 'created_at', 'updated_at']
        # Задаем поля, которые будут только для чтения (read-only)
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at']

# Определяем сериализатор для модели Category
class CategorySerializer(serializers.ModelSerializer):
    # Внутренний класс Meta для указания метаданных
    class Meta:
        # Указываем модель, которую будем сериализовать
        model = Category
        # Задаем поля, которые будут включены в сериализацию
        fields = ['id', 'name']

# Определяем сериализатор для модели Priority
class PrioritySerializer(serializers.ModelSerializer):
    # Внутренний класс Meta для указания метаданных
    class Meta:
        # Указываем модель, которую будем сериализовать
        model = Priority
        # Задаем поля, которые будут включены в сериализацию
        fields = ['id', 'name']

# Определяем сериализатор для регистрации пользователя
class RegisterSerializer(serializers.ModelSerializer):
    # Поле password для ввода пароля, установлено как write_only (только для записи)
    password = serializers.CharField(write_only=True)

    # Внутренний класс Meta для указания метаданных
    class Meta:
        # Указываем модель, которую будем сериализовать
        model = User
        # Задаем поля, которые будут включены в сериализацию
        fields = ['username', 'email', 'password']

    # Метод create для создания нового пользователя
    def create(self, validated_data):
        # Создаем нового пользователя с помощью метода create_user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # Возвращаем созданного пользователя
        return user
