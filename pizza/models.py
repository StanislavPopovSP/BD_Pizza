from django.db import models
from django.core.validators import RegexValidator


class Pizza(models.Model):
    """Работа с Пиццей"""
    title = models.CharField(max_length=200, null=True, blank=True)  # название
    dough = models.CharField(max_length=200, null=True, blank=True)  # тесто
    filling = models.CharField(max_length=200, null=True, blank=True)  # начинка
    sauce = models.CharField(max_length=200, null=True, blank=True)  # соус
    weight = models.FloatField(default=0, null=True, blank=True)  # вес
    price = models.FloatField(default=0, null=True, blank=True)  # цена
    pizza_image = models.ImageField(blank=True, null=True, upload_to='pizza/', default='')  # фото пиццы

    def __str__(self):
        """Заголовок проекта"""
        return f'{self.title}'


class Orders(models.Model):
    """Время создания пиццы"""
    pizza = models.ForeignKey(Pizza, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.ForeignKey(Pizza, on_delete=models.SET_NULL, null=True, blank=True, related_name='prices')
    created = models.DateTimeField(auto_now_add=True) # Автоматическое создание времени и даты ордера

    def __str__(self):
        """Пицца"""
        return f'{self.pizza}'


class Seller(models.Model):
    """Продавец"""
    AGE = (
        ('m', 'male'),
        ('zh', 'woman')
    )
    firstname = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    age = models.DateField(null=True, blank=True)
    floor = models.CharField(max_length=200, choices=AGE) # пол
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$") # здесь можно настроить из шаблона то что надо, данный шаблон идёт по умолчанию(формат E.164).

    def __str__(self):
        """Пицца"""
        return f'{self.firstname}'


class Day(models.Model):
    """День открытия и закрытия магазина продавцом"""
    owner = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)
    date = models.DateField(null=True, blank=True) # Выбор даты
    opening_date = models.DateTimeField(null=True, blank=True) # Выбор времени открытия
    date_completed = models.DateTimeField(null=True, blank=True) # Выбор времени закрытия

    def __str__(self):
        """Время открытия"""
        return f'{self.opening_date}'