from rest_framework import serializers
from .models import *


#! Сериализатор полного профиля пользователя
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


#! Сериализатор страны (с изображением)
class CountryUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["country_name", "country_image"]


#! Сериализатор пользователя с вложенной страной
class UserProfileCountrySerializer(serializers.ModelSerializer):
    country = CountryUserSerializer()

    class Meta:
        model = UserProfile
        fields = ["user_name", "country"]


#! Упрощённый сериализатор профиля пользователя
class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["first_name", "last_name"]


#! Сериализатор полной информации о стране
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


#! Упрощённый сериализатор страны
class CountrySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["country_name"]


#! Упрощённый сериализатор города
class CitySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["city_name"]


#! Сериализатор изображения отеля
class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ["hotel_image"]


#! Сериализатор изображения комнаты
class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ["room_image"]


#! Сериализатор отзыва
class ReviewSerializer(serializers.ModelSerializer):
    user_name = (
        UserProfileCountrySerializer()
    )  

    class Meta:
        model = Review
        fields = ["user_name", "text", "stars"]


#! Сериализатор комнаты с изображениями
class RoomSerializer(serializers.ModelSerializer):
    room_images = RoomImageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = [
            "id",
            "room_number",
            "room_type",
            "room_status",
            "room_price",
            "room_images",
        ]


#! Сериализатор списка отелей
class HotelListSerializer(serializers.ModelSerializer):
    hotel_images = HotelImageSerializer(many=True, read_only=True)
    city = CitySimpleSerializer()
    avg_rating = serializers.SerializerMethodField()
    count_people = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = [
            "id",
            "hotel_name",
            "city",
            "address",
            "hotel_stars",
            "hotel_images",
            "avg_rating",
            "count_people",
        ]

    def get_avg_rating(self, obj):
        return obj.avg_rating()

    def get_count_people(self, obj):
        return obj.count_people()


#! Сериализатор детальной информации об отеле
class HotelDetailSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(many=True, read_only=True)
    avg_rating = serializers.SerializerMethodField()
    count_people = serializers.SerializerMethodField()
    owner = UserProfileSimpleSerializer()
    country = CountrySimpleSerializer()
    city = CitySimpleSerializer()
    hotel_images = HotelImageSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = [
            "hotel_name",
            "owner",
            "hotel_description",
            "country",
            "city",
            "address",
            "hotel_stars",
            "hotel_images",
            "hotel_video",
            "created_date",
            "rooms",
            "reviews",
            "avg_rating",
            "count_people",
        ]

    def get_avg_rating(self, obj):
        return obj.avg_rating()

    def get_count_people(self, obj):
        return obj.count_people()


#! Сериализатор бронирования
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking  
        fields = "__all__"
