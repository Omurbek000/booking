from rest_framework import viewsets, generics
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend  #! фильтр для поиска
from rest_framework.filters import SearchFilter, OrderingFilter  #! для поиска по полям
from .filters import HotelFilter,  RoomFilter #! импортируем фильтр для поиска

# Create your views here.


class UserProfileViewset(viewsets.ModelViewSet): #! класс для работы с пользователями
    queryset = UserProfile.objects.all() #! все объекты модели 
    serializer_class = UserProfileSerializer #! сериализатор


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter,
    ]  #! фильтр для поиска указывает, что мы хотим использовать фильтр для поиска
    filterset_class = HotelFilter
    ordering_fields = ['hotel_stars']  #! сортировка по полям
    search_fields = ['hotel_name']  #! поиск по полям 


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]  #! фильтр для поиска
    filter_class =  RoomFilter  #! фильтр для поиска
    ordering_fields = ['room_price']  #! сортировка по полям
    search_fields = ['room_number']  #! поиск по полям 


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
