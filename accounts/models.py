from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.fields import BooleanField
from datetime import datetime, timedelta
from django.conf import settings

from core.models import TimestampedModel


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('이름은 필수값입니다.')
        if email is None:
            raise TypeError('이메일은 필수값입니다.')
        if password is None:
            raise TypeError('비밀번호는 필수값입니다.')

        user = self.model(
            username=username,
            # 이메일 정규화 >> 중복 최소화
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):

        user = self.create_user(username, email, password)

        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin, TimestampedModel):

    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
    ]

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username
