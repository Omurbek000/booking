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
  adres = models.CharField(max_length=64)
  hotrl_video = models.FieldFile(upload_to='videos/')
  created_date = models.DateTimeField(auto_created=True)
  
  def __str__(self) -> str:
    return f"{self.hotel_name} , {self.country}, {self.city} "
  
  
class HotelImage(models.Model):
  hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
  hotel_image = models.ImageField(upload_to='images/', null=True, blank=True)
  
class Room(models.Model):
  pass   