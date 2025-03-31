# Импортируем сигнал post_save из django.db.models.signals
from django.db.models.signals import post_save
# Импортируем декоратор receiver из django.dispatch для обработки сигналов
from django.dispatch import receiver
# Импортируем модель User из django.contrib.auth.models для работы с пользователями
from django.contrib.auth.models import User
# Импортируем модель Token из rest_framework.authtoken.models для работы с токенами аутентификации
from rest_framework.authtoken.models import Token

# Определяем функцию create_auth_token с использованием декоратора receiver для обработки сигнала post_save, отправленного моделью User
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    # Если пользователь был создан (created=True)
    if created:
        # Создаем токен аутентификации для нового пользователя
        Token.objects.create(user=instance)
