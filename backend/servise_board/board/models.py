import os

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
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Фото')

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


class OrderStatus(models.Model):
    status = models.CharField(max_length=200, verbose_name='Статус')

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказов'


class Order(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    detail = models.TextField(verbose_name='Описане')
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Заказчик')
    status = models.ForeignKey(to=OrderStatus, on_delete=models.PROTECT, verbose_name='Статус')

    def delete(self, *args, **kwargs):
        for photo in self.orderphoto_set.all():
            photo.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Media(models.Model):
    file: models.ImageField | models.FileField = None
    source: models.ForeignKey = None

    def filename(self):
        return os.path.basename(self.photo.name)

    def delete(self, *args, **kwargs):
        photo_path = self.photo.path
        os.remove(photo_path)
        super().delete(*args, **kwargs)


class OrderPhoto(Media):
    file = models.ImageField(upload_to='orders/photos/', verbose_name='Фото')
    source = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name='Заказ')


class OrderVideo(Media):
    file = models.FileField(upload_to='orders/videos/', verbose_name='Видео')
    source = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name='Заказ')
