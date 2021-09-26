import csv
from django.shortcuts import render, redirect
from .models import Setting, ClimateData
from .forms import SingleFileForm
from .weather_utils import get_forecast_data
from .telegram_utils import send_test_notification

# main page views


def alarms_view(request):
    # getting setting for alarms
    setting = Setting.objects.first()
    return render(request, 'user_dashboard/alarms.html', context={'setting': setting})


def test_alarm_view(request):
    # getting setting for alarms
    setting = Setting.objects.first()
    send_test_notification(
        setting.telegram_api_token, setting.telegram_chat_id)
    return redirect('alarms')


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


def climate_view(request):

    # handle climate data upload
    if request.method == 'POST':

        form = SingleFileForm(request.POST, request.FILES)
        if form.is_valid():
            # form is valid, upload climate data to db
            file = request.FILES['csv']
            decoded_file = file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            for row in reader:
                cell_values = list(row.values())
                ClimateData.objects.create(
                    date=cell_values[0],  # get date
                    temp=cell_values[1],  # get temp
                    rain=cell_values[2],  # get rain
                )

    # send climate data and empty form
    climate_data = ClimateData.objects.all()
    rain = []
    dates = []
    temp = []
    for d in climate_data:
        rain.append(d.rain)
        dates.append(d.date)
        temp.append(d.temp)

    form = SingleFileForm()
    return render(request, 'user_dashboard/climate.html', context={
        'form': form,
        'data': {
            'rain': rain,
            'temp': temp,
            'dates': dates,
        }
    })


def delete_climate_data(request):
    ClimateData.objects.all().delete()
    return redirect('climate')


# alarm activate/deactivate views
# precipitation
def toggle_precipitation_alarm(request):
    setting = Setting.objects.first()
    setting.precipitation_alarm = not setting.precipitation_alarm
    setting.save()
    return redirect('alarms')


# heat
def toggle_heat_alarm(request):
    setting = Setting.objects.first()
    setting.heat_alarm = not setting.heat_alarm
    setting.save()
    return redirect('alarms')

# frost
def toggle_frost_alarm(request):
    setting = Setting.objects.first()
    setting.frost_alarm = not setting.frost_alarm
    setting.save()
    return redirect('alarms')
