from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator


#! 🌍 Модель страны
class Country(models.Model):
    country_name = models.CharField(max_length=32, unique=True)  #! Название страны
    country_image = models.ImageField(
        upload_to="country_images/"
    )  #! Флаг или изображение страны

    def __str__(self):
        return self.country_name


#! 👤 Расширенная модель пользователя
class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ("simpleUser", "Обычный пользователь"),
        ("ownerUser", "Владелец отеля"),
    )
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE
    )  #! Страна пользователя
    user_role = models.CharField(
        max_length=10, choices=ROLE_CHOICES, default="simpleUser"
    )  #! Роль пользователя
    phone_number = PhoneNumberField(region="RUS")  #! Номер телефона
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(100)]
    )  #! Возраст

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


#! 🏙️ Модель города
class City(models.Model):
    city_name = models.CharField(max_length=32, unique=True)  #! Название города

    def __str__(self):
        return self.city_name


#! 🏨 Модель отеля
class Hotel(models.Model):
    hotel_name = models.CharField(max_length=32)  #! Название отеля
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  #! Владелец отеля
    hotel_description = models.TextField()  #! Описание отеля
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE
    )  #! Страна, где расположен отель
    city = models.ForeignKey(City, on_delete=models.CASCADE)  #! Город
    address = models.CharField(max_length=64)  #! Адрес
    hotel_stars = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )  #! Кол-во звёзд
    hotel_video = models.FileField(
        upload_to="videos/", null=True, blank=True
    )  #! Видео-презентация отеля
    created_date = models.DateTimeField(auto_now_add=True)  #! Дата создания

    def __str__(self):
        return f"{self.hotel_name} ({self.city}, {self.country})"

    def avg_rating(self):
        """📊 Расчёт среднего рейтинга отеля"""
        ratings = self.reviews.all()
        if ratings.exists():
            return round(sum([r.stars for r in ratings]) / ratings.count(), 2)
        return 0

    def count_people(self):
        """👥 Количество пользователей, оставивших отзывы"""
        return self.reviews.count()


#! 🖼️ Модель изображений отеля
class HotelImage(models.Model):
    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, related_name="hotel_images"
    )  #! Связь с отелем
    hotel_image = models.ImageField(
        upload_to="hotel_images/", null=True, blank=True
    )  #! Фото отеля


#! 🚪 Модель комнаты
class Room(models.Model):
    room_number = models.PositiveSmallIntegerField()  #! Номер комнаты
    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, related_name="rooms"
    )  #! Отель, к которому относится комната

    TYPE_ROOM = (
        ("люкс", "Люкс"),
        ("семейный", "Семейный"),
        ("одноместный", "Одноместный"),
        ("двухместный", "Двухместный"),
    )
    room_type = models.CharField(max_length=12, choices=TYPE_ROOM)  #! Тип комнаты

    STATUS_CHOICES = (
        ("доступен", "Доступен"),
        ("забронирован", "Забронирован"),
    )
    room_status = models.CharField(
        max_length=12, choices=STATUS_CHOICES
    )  #! Статус комнаты

    room_price = models.PositiveSmallIntegerField()  #! Цена за ночь
    all_included = models.BooleanField(
        default=False
    )  #! Включено ли всё (питание, удобства)
    room_description = models.TextField()  #! Описание комнаты

    def __str__(self):
        return f"Комната {self.room_number} в {self.hotel.hotel_name}"


#! 🖼️ Модель изображений комнаты
class RoomImage(models.Model):
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name="room_images"
    )  #! Связь с комнатой
    room_image = models.ImageField(
        upload_to="room_images/", null=True, blank=True
    )  #! Фото комнаты


#! 📝 Модель отзыва
class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  #! Автор отзыва
    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, related_name="reviews"
    )  #! Отель, к которому относится отзыв
    text = models.TextField()  #! Текст отзыва
    stars = models.PositiveSmallIntegerField(
        choices=[(i, str(i)) for i in range(1, 11)], null=True, blank=True
    )  #! Оценка от 1 до 10

    def __str__(self):
        return f"{self.user.username} → {self.hotel.hotel_name}: {self.stars}★"


#! 📅 Модель бронирования
class Booking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)  #! Забронированный отель
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  #! Забронированная комната
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE
    )  #! Пользователь, сделавший бронирование
    check_in = models.DateTimeField()  #! Дата заезда
    check_out = models.DateTimeField()  #! Дата выезда
    total_price = models.PositiveSmallIntegerField(default=0)  #! Общая стоимость

    STATUS_CHOICES = (
        ("забронирован", "Забронирован"),
        ("отменен", "Отменён"),
    )
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES
    )  #! Статус бронирования

    def __str__(self):
        return f"{self.user.username} → {self.hotel.hotel_name} / Комната {self.room.room_number} ({self.status})"
