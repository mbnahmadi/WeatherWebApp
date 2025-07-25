"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('get_weather/', views.get_weather_latlon_view, name='get_weather_latlon'),
    path('search_city/', views.search_city_view, name='search_city'),
    path('get_forecast/', views.get_forecast_view, name='get_forecast'),
    path('forecast/', views.weatherforecast_view, name='get_forecast'),
]
