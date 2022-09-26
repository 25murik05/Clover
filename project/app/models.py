from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,PermissionsMixin)
from django.contrib.auth import get_user_model


class UserManager(BaseUserManager):
    """
    Django требует, чтобы кастомные пользователи определяли свой собственный
    класс Manager. Унаследовавшись от BaseUserManager, мы получаем много того
    же самого кода, который Django использовал для создания User (для демонстрации).
    """

    def create_user(self, name, email, password=None):
        """ Создает и возвращает пользователя с имэйлом, паролем и именем. """

        user = self.model(name=name, email=self.normalize_email(email),)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):
        """ Создает и возввращет пользователя с привилегиями суперадмина. """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255, null=True, unique=True)
    email = models.EmailField(db_index=True, unique=True, blank=True, null=True)
    # Этот флаг определяет, кто может войти в административную часть нашего
    # сайта. Для большинства пользователей это флаг будет ложным.
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        """ Строковое представление модели (отображается в консоли) """
        return self.email


class Certificate(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=255, unique=True, db_index=True, blank=True, null=True)

    def __str__(self):
        return self.number