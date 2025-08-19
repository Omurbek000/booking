from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator


class UserProfile(AbstractUser):
  ROLE_CHOICES = (
    ('simpleUser', 'simpleUser'),
    ('ownerUser', 'ownerUser'),
  )
  user_role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='simpleUser')
  phone_number = PhoneNumberField(region='RUS')
  age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18), MaxValueValidator(100)])


  def __str__(self):
    return f"{self.first_name}: {self.last_name} " 


class Country(models.Model):
  country_name = models.CharField(max_length=32, unique=True)
  
  def __str__(self) -> str:
    return f"{self.country_name} "
  

class City(models.Model):
  city_name = models.CharField(max_length=32, unique=True)
  
  def __str__(self) -> str:
    return f"{self.city_name} "
 
 
class Hotel(models.Model):
  hotel_name = models.CharField(max_length=32)
  owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
  hotel_descriptions = models.TextField()
  country = models.ForeignKey(Country, on_delete=models.CASCADE)
  city = models.ForeignKey(City, on_delete=models.CASCADE)
  address = models.CharField(max_length=64)
  hotel_stars = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
  hotel_video = models.FieldFile(upload_to='videos/', null=True, blank=True)
  created_date = models.DateTimeField(auto_created=True)
  
  def __str__(self) -> str:
    return f"{self.hotel_name} , {self.country}, {self.city} "
  
  
class HotelImage(models.Model):
  hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
  hotel_image = models.ImageField(upload_to='images/', null=True, blank=True)
  
class Room(models.Model):
  room_number = models.PositiveSmallIntegerField()
  hotel_room = models.ForeignKey(Hotel, on_delete=models.CASCADE)
  TYPE_ROOM = (
    ('люкс', 'люкс'),
    ('семейный', 'семейный'),
    ('одноместный', 'одноместный'),
    ('двухместный', 'двухместный'),
  )
  room_type = models.CharField(max_length=10, choices=TYPE_ROOM)
  STATUS_CHOICES = (
    ('доступен', 'доступен'),
    ('забронирован', 'забронирован'),
  )
  room_status = models.CharField(max_length=10, choices=STATUS_CHOICES)
  room_price = models.PositiveSmallIntegerField()
  all_includest = models.BooleanField(default=False)
  room_descriptions = models.TextField()

  def __str__(self) -> str:
    return f"{self.user_name} {self.hotrl} {self.stars}"


class RoonImage(models.Model):
  room = models.ForeignKey(Room, on_delete=models.CASCADE),
  romm_image = models.ImageField(upload_to='images/', null=True, blank=True)
  
  
class Review(models.Model):
  user_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
  hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
  text = models.PositiveSmallIntegerField()
  stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for in range(1,6)], null=True, blank=True)
  
  def __str__(self) -> str:
    return f"{self.user_name} {self.hotrl} {self.stars}"

class Boking(models.Model):
  hotrl_book = models.ForeignKey(Hotel, on_delete=models.CASCADE)
  room_book = models.ForeignKey(Room, on_delete=models.CASCADE)
  user_book = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
  check_in = models.DateTimeField()
  check_out = models.DateTimeField()
  total_price = models.PositiveSmallIntegerField(default=0)
  STATUS_CHOICES = (
    ('забронирован', 'забронирован'),
    ('отменен', 'отменен'),
  )
  status_book = models.CharField(max_length=10, choices=STATUS_CHOICES)
  
  def __str__(self) -> str:
    return f"{user_book} {self.hotel_book} {self.room_book} {self.status_book}"
  