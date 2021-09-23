from django.db import models


class Setting(models.Model):
    # admin settings
    location_latitude = models.CharField(max_length=10, default='67.0822')
    location_longitude = models.CharField(max_length=10, default='24.9056')

    open_weather_key = models.CharField(max_length=101, default='-')

    telegram_chat_id = models.CharField(max_length=101, default='-')
    telegram_api_token = models.CharField(max_length=101, default='-')

    # user settings
    precipitation_alarm = models.BooleanField(default=True)
    heat_alarm = models.BooleanField(default=True)
    frost_alarm = models.BooleanField(default=True)

    def __str__(self):
        return "App Configuration"


class ClimateData(models.Model):
    date = models.CharField(max_length=11)
    temp = models.FloatField()
    rain = models.FloatField()
