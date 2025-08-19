from django.urls import path , include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter() #! создаем роутер
router.register(r'user_profile', UserProfileViewset, basename='user_profile'), #! регистрация роутера
router.register(r'country', CountryViewSet, basename='country'), 
router.register(r'city', CityViewSet, basename='city'),
router.register(r'hotel', HotelViewSet, basename='hotel'),
router.register(r'room', RoomViewSet, basename='room'),
router.register(r'review', ReviewViewSet, basename='review'),
router.register(r'booking', BookingViewSet, basename='booking'),


urlpatterns = [
    path('', include(router.urls))
] #! добавляем роутер в urlpatterns
