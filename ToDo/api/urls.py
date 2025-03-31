from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, CategoryViewSet, PriorityViewSet, UserViewSet, register_view, task_list_view
from .views import create_task_view, edit_task_view, delete_task_view
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'priorities', PriorityViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', register_view, name='register'),
    path('api/', include(router.urls)),
    path('tasks/', task_list_view, name='tasks'),
    path('tasks/create/', create_task_view, name='create_task'),
    path('tasks/edit/<int:pk>/', edit_task_view, name='edit_task'),
    path('tasks/delete/<int:pk>/', delete_task_view, name='delete_task'),

]


