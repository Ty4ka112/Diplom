from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import register_view, task_list_view, create_task_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', register_view, name='register'),
    path('api/', include('api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tasks/', task_list_view, name='tasks'),  # Маршрут для отображения списка задач
    path('tasks/create/', create_task_view, name='create_task'),  # Добавлен маршрут для создания задачи
]
