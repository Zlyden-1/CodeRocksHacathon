from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    patronimic = models.CharField(max_length=100, blank=True, null=True, verbose_name='Отчество')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Почта')
    about = models.TextField(blank=True, null=True, verbose_name='О себе')
    city = models.CharField(max_length=200, verbose_name='Город')

    class Meta:
        permissions = ()


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Contractor(User):
    categories = models.ManyToManyField(Category)

    class Meta:
        permissions = ()





