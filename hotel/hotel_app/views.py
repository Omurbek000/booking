from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import *
from .serializers import *
from .filters import HotelFilter, RoomFilter

#! 👤 ViewSet для работы с профилем текущего пользователя
class UserProfileViewset(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        #! Возвращает только профиль текущего пользователя
        return UserProfile.objects.filter(id=self.request.user.id)


#! 🌍 ViewSet для стран (список, создание, редактирование, удаление)
class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySimpleSerializer


#! 🏙️ ViewSet для городов
class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySimpleSerializer


#! 🏨 APIView для списка отелей с фильтрацией, поиском и сортировкой
class HotelListApiView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = HotelFilter  #! Фильтрация по полям (например, по стране, городу)
    ordering_fields = ["hotel_stars"]  #! Сортировка по количеству звёзд
    search_fields = ["hotel_name"]  #! Поиск по названию отеля


#! 🏨 APIView для получения детальной информации об отеле
class HotelDetailApiView(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer


#! 🚪 ViewSet для комнат
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


#! 📝 ViewSet для отзывов с фильтрацией и поиском
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = RoomFilter  
    ordering_fields = ["stars"]  #! Сортировка по рейтингу
    search_fields = ["text"]  #! Поиск по содержанию отзыва


#! 📅 ViewSet для бронирований
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer











# from rest_framework import viewsets, generics
# from .models import *
# from .serializers import *
# from django_filters.rest_framework import DjangoFilterBackend  #! фильтр для поиска
# from rest_framework.filters import SearchFilter, OrderingFilter  #! для поиска по полям
# from .filters import HotelFilter, RoomFilter  #! импортируем фильтр для поиска

# # Create your views here.


# class UserProfileViewset(viewsets.ModelViewSet):  #! класс для работы с пользователями
#     queryset = UserProfile.objects.all()  #! все объекты модели
#     serializer_class = UserProfileSerializer  #! сериализатор

#     def get_queryset(self):  #! метод для получения объектов
#         return UserProfile.objects.filter(id=self.request.user.id)


# class CountryViewSet(viewsets.ModelViewSet):
#     queryset = Country.objects.all()
#     serializer_class = CountrySimpleSerializer


# class CityViewSet(viewsets.ModelViewSet):
#     queryset = City.objects.all()
#     serializer_class = CitySimpleSerializer


# class HotelListApiView(generics.ListAPIView):
#     queryset = Hotel.objects.all()
#     serializer_class = HotelListSerializer
#     filter_backends = [
#         DjangoFilterBackend,
#         OrderingFilter,
#         SearchFilter,
#     ]  #! фильтр для поиска указывает, что мы хотим использовать фильтр для поиска
#     filterset_class = HotelFilter
#     ordering_fields = ["hotel_stars"]  #! сортировка по полям
#     search_fields = ["hotel_name"]  #! поиск по полям


# class HotelDetailAPiView(generics.RetrieveAPIView):
#     queryset = Hotel.objects.all()
#     serializer_class = HotelDetailSerializer

   

# class RoomViewSet(viewsets.ModelViewSet):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer


# class ReviewViewSet(viewsets.ModelViewSet):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     filter_backends = [
#         DjangoFilterBackend,
#         OrderingFilter,
#         SearchFilter,
#     ]  #! фильтр для поиска
#     filter_class = RoomFilter  #! фильтр для поиска
#     ordering_fields = ["room_price"]  #! сортировка по полям
#     search_fields = ["room_number"]  #! поиск по полям


# class BookingViewSet(viewsets.ModelViewSet):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer
