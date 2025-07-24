from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
import requests
from django.conf import settings
# Create your views here.


def home_view(request):
    return render(request, 'weatherapp/home.html', {})



def weatherforecast_view(request):
    return render(request, 'weatherapp/home.html', {})


def get_weather_latlon_view(request):
    lat = request.GET.get("lat")
    lon = request.GET.get("lon")
    api_key = settings.OPENWEATHER_API_KEY

    if not lat or not lon:
        return JsonResponse({"error": "Missing latitude or longitude"}, status=400)

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

    response = requests.get(url)
    return JsonResponse(response.json())


def search_city_view(request):
    city = request.GET.get("q")
    api_key = settings.OPENWEATHER_API_KEY

    if not city:
        return JsonResponse({"error": "City name is required!"}, status=400)

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return JsonResponse({"error": "City not found"}, status=404)

    return JsonResponse(response.json())


@login_required(login_url='login')
def get_forecast_view(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    api_key = settings.OPENWEATHER_API_KEY

    if not lat or not lon:
        return JsonResponse({'error': 'Coordinates are invalid'}, status=400)

    try:
        url = "https://api.openweathermap.org/data/2.5/forecast"
        params = {
            'lat': lat,
            'lon': lon,
            'units': 'metric',
            'appid': api_key,
            # 'lang': 'fa'
        }

        response = requests.get(url, params=params)
        if response.status_code != 200:
            return JsonResponse({'error': f'API error: {response.json().get("message", 'unknown problem')}'}, status=response.status_code)

        data = response.json()
        forecast_list = data.get("list", [])
        if not forecast_list:
            return JsonResponse({'error': 'No data found for prediction'}, status=404)

        daily_data = [forecast_list[i] for i in range(0, len(forecast_list), 8)]
        return JsonResponse({'daily': daily_data})

    except Exception as e:
        return JsonResponse({'error': f'Error processing request: {str(e)}'}, status=500)