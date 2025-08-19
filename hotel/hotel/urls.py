"""
URL configuration for hotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns #! импортируем i18n_patterns
from django.contrib import admin #! импортируем админку
from django.urls import path, include #! импортируем path
from django.conf import settings #! импортируем настройки 
from django.conf.urls.static import static #! импортируем статику
from drf_yasg.views import get_schema_view #! импортируем get_schema_view
from drf_yasg import openapi #! импортируем openapi
from rest_framework import permissions №! импортируем разрешения для swagger


schema_view = get_schema_view( 
    openapi.Info( 
        title="Booking.com",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
) # ! схема для документации swagger 

urlpatterns = [
    path('admin/', admin.site.urls), # ! путь к админке
    path('', include('hotel_app.urls')), #! импортируем url из приложения
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'), #! документация swagger
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #! статика
