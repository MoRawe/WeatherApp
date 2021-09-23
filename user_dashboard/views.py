from django.shortcuts import render

def forecast_view(request):
    # getting forecast data
    setting = Setting.objects.first()
    forecast_data = get_forecast_data(
        setting.open_weather_key,
        setting.location_latitude,
        setting.location_longitude
    )

    if not forecast_data:
        # if no forecast data available return empty view
        return render(request, 'user_dashboard/forecast.html')

    # return view with forecast data
    return render(request, 'user_dashboard/forecast.html', context={'forecast': forecast_data})
