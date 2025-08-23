# from django.contrib import admin
# from .models import *
# from modeltranslation.admin import TranslationAdmin

# # Register your models here.

# @admin.register(Country, City)  #! класс регистрации
# class ProductAdmin(TranslationAdmin):  #! класс админки
#     class Media:  #! класс медиа
#         js = (
#             "http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
#             "http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
#             "modeltranslation/js/tabbed_translation_fields.js",
#         )
#         css = {
#             "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
#         }


# class HotelImageInline(
#     admin.TabularInline
# ):  #! класс для отображения картинок в админке
#     model = HotelImage  #! модель
#     extra = 1  #! количество картинок


# class RoomImageInline(admin.TabularInline):
#     model = RoomImage
#     extra = 1


# @admin.register(Hotel)  #! класс регистрации
# class ProductAdmin(TranslationAdmin):  #! класс админки
#     inlines = [HotelImageInline]  #! вложенные инлайн

#     class Media:
#         js = (
#             "http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
#             "http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
#             "modeltranslation/js/tabbed_translation_fields.js",
#         )
#         css = {
#             "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
#         }


# @admin.register(Room)
# class ProductAdmin(TranslationAdmin):
#     inlines = [RoomImageInline]

#     class Media:
#         js = (
#             "http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
#             "http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
#             "modeltranslation/js/tabbed_translation_fields.js",
#         )
#         css = {
#             "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
#         }


# admin.site.register(UserProfile)  #! регистрация модели
# admin.site.register(Review)
# admin.site.register(Booking)




from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

@admin.register(Country, City)
class CountryCityAdmin(TranslationAdmin):
    class Media:
        js = (
            "http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }

class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 1

class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 1

@admin.register(Hotel)
class HotelAdmin(TranslationAdmin):
    inlines = [HotelImageInline]
    class Media:
        js = (
            "http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }

@admin.register(Room)
class RoomAdmin(TranslationAdmin):
    inlines = [RoomImageInline]
    class Media:
        js = (
            "http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }

admin.site.register(UserProfile)
admin.site.register(Review)
admin.site.register(Booking)