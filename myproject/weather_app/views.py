from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def weather(request):
    weather_data = None  # Default value

    if request.method == 'POST':
        city = request.POST.get('city', '')  # Get city safely
        country = request.POST.get('country', '')  # Get country safely

        if city and country:
            api_key = 'a776b788a108d646abc5a57335224f31'
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}'

            try:
                response = requests.get(url)
                response.raise_for_status()  # Raise error if request fails
                list_of_data = response.json()
                print(list_of_data)  # Debugging line to check the response
                weather_data = {
                    'city': list_of_data.get('name', 'Unknown'),
                    'country': list_of_data.get('sys', {}).get('country', 'Unknown'),
                    'temperature': round(list_of_data.get('main', {}).get('temp', 273.15) - 273.15, 2),
                    'pressure': list_of_data.get('main', {}).get('pressure', 'N/A'),
                    'humidity': list_of_data.get('main', {}).get('humidity', 'N/A'),
                    'description': list_of_data.get('weather', [{}])[0].get('description', 'N/A'),
                }
            except requests.exceptions.RequestException as e:
                weather_data = {'error': f"API request failed: {e}"}

    return render(request, 'weather_app/index.html', {'weather_data': weather_data})
