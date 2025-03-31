from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, generics
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Task, Category, Priority
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import TaskSerializer, CategorySerializer, PrioritySerializer, UserSerializer, RegisterSerializer
from .forms import TaskForm


def delete_task_view(request, pk):
    task = get_object_or_404(Task, pk=pk, created_by=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    return render(request, 'delete_task.html', {'task': task})

def edit_task_view(request, pk):
    task = get_object_or_404(Task, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')  # Перенаправление на список задач
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'task': task})


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
        return Response({'status': 'password reset', 'new_password': new_password})

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})  # Без вложенных директорий


def task_list_view(request):
    tasks = Task.objects.filter(created_by=request.user)
    return render(request, 'tasks.html', {'tasks': tasks})


def create_task_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            return redirect('tasks')
        else:
            print(form.errors)
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

