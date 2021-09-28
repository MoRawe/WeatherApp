from django.urls import path
from .views import (
    alarms_view,
    test_alarm_view,

    forecast_view,

    climate_view,
    delete_climate_data,

    toggle_precipitation_alarm,
    toggle_heat_alarm,
    toggle_frost_alarm,
)

urlpatterns = [
    # main pages routes
    path('', alarms_view, name='alarms'),
    path('send_test_alarm/', test_alarm_view, name='test_alarm'),

    path('forecast/', forecast_view, name='forecast'),

    path('climate/', climate_view, name='climate'),
    path('climate/delete/', delete_climate_data, name='delete_climate'),

    # alarm toggle activate/deactivate routes
    path('toggle_precipitation_alarm/', toggle_precipitation_alarm,
         name='toggle_precipitation_alarm'),
    path('toggle_heat_alarm/', toggle_heat_alarm, name='toggle_heat_alarm'),
    path('toggle_frost_alarm/', toggle_frost_alarm, name='toggle_frost_alarm'),
]
