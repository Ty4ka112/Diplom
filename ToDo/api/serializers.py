from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task, Category, Priority

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'created_by', 'title', 'description', 'status', 'completed', 'created_at', 'completed_at', 'updated_at', 'deleted_at', 'deleted', 'category', 'priority']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'deleted_at', 'deleted']

class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = ['id', 'name', 'created_at', 'updated_at', 'deleted_at', 'deleted']
