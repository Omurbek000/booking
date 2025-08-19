from django_filters import FilterSet  #! импортируем FilterSet
from .models import Room, Hotel  #! импортируем модели


class HotelFilter(FilterSet):  #! создаем класс HotelFilter
    class Meta:  #! создаем класс Meta
        model = Hotel  #! указываем модель
        fields = {
            "hotel_name": ["exact"],  #! фильтруем по названию отеля
            "country": ["exact"],  #! фильтруем по стране
            "city": ["exact"],  #! фильтруем по городу
            "hotel_stars": ["gt", "lt"],  #! фильтруем по количеству звезд
        }  #! фильтруем по названию,


class RoomFilter(FilterSet):  #! создаем класс RoomFilter
    class Meta:  #! создаем класс Meta
        model = Room  #! указываем модель
        fields = {
            "room_number": ["exact"],  #! фильтруем по номеру комнаты
            "room_type": ["exact"],  #! фильтруем по типу комнаты
            "room_status": ["exact"],  #! фильтруем по статусу комнаты
            "room_price": ["gt", "lt"],  #! фильтруем по цене комнаты
        }
