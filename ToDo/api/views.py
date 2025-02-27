from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Task, Category, Priority
from .serializers import TaskSerializer, CategorySerializer, PrioritySerializer, UserSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status', 'category', 'priority']
    ordering_fields = ['created_at', 'status']

    def get_queryset(self):
        if self.request.user.is_staff:
            return Task.objects.all()
        return Task.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Category.objects.all()
        return Category.objects.filter(created_by=self.request.user)

class PriorityViewSet(viewsets.ModelViewSet):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Priority.objects.all()
        return Priority.objects.filter(created_by=self.request.user)

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
