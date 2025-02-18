from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from .models import Task, Category, Priority
from .serializers import TaskSerializer, CategorySerializer, PrioritySerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(created_by=user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsOwnerOrReadOnly]

class PriorityViewSet(viewsets.ModelViewSet):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
    permission_classes = [IsOwnerOrReadOnly]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        user = serializer.save()
        Token.objects.create(user=user)

    @action(detail=False, methods=['post'])
    def change_password(self, request):
        user = request.user
        user.set_password(request.data['new_password'])
        user.save()
        return Response({'status': 'password set'})

    @action(detail=False, methods=['post'])
    def reset_password(self, request):
        user = User.objects.get(email=request.data['email'])
        new_password = User.objects.make_random_password()
        user.set_password(new_password)
        user.save()
        # Здесь вы можете отправить новый пароль пользователю по электронной почте
        return Response({'status': 'password reset', 'new_password': new_password})
