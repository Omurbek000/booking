from rest_framework import serializers
from .models import *

class UserProfileSerializer(serializers.ModelSerializer): #! получаем данные из модели
    class Meta: #! класс метаданные
    model = UserProfile #! модель
    fields = '__all__' #! все поля в модели которые мы хотим получить


class CountrySerializer(serializers.ModelSerializer): #! получаем данные из модели
    class Meta: #! класс метаданные
    model = Country #! модель
    fields = '__all__' #! все поля в модели которые мы хотим получить


class CitySerializer(serializers.ModelSerializer):  #! получаем данные из модели
    class Meta:   #! класс метаданные
    model = City  #! модель
    fields = '__all__'  #! все поля в модели которые мы хотим получить


class HotelSerializer(serializers.ModelSerializer):   #! получаем данные из модели
    class Meta:   #! класс метаданные
    model = Hotel   #! модель
    fields = '__all__'  #! все поля в модели которые мы хотим получить


class RoomSerializer(serializers.ModelSerializer):  #! получаем данные из модели
    class Meta:  #! класс метаданные
    model = Room  #! модель
    fields = '__all__'  #! все поля в модели которые мы хотим получить


class ReviewSerializer(serializers.ModelSerializer):  #! получаем данные из модели
    class Meta:  #! класс метаданные
    model = Review  #! модель
    fields = '__all__'  #! все поля в модели которые мы хотим получить


class BokingSerializer(serializers.ModelSerializer):  #! получаем данные из модели
    class Meta:  #! класс метаданные
    model = Boking  #! модель
    fields = '__all__'  #! все поля в модели которые мы хотим получить