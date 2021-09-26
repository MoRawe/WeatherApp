from .weather_utils import get_tomorrow_forecast, get_next_hour_forecast
from .telegram_utils import send_telegram_notification
from .models import Setting


def hourly_alarms():
    '''
    Sends hourly alarm:
    '''

    setting = Setting.objects.first()

    # check if alarm is activated
    if not setting.precipitation_alarm:
        return

    api_key = setting.open_weather_key
    lat = setting.location_latitude
    lon = setting.location_longitude

    result = get_next_hour_forecast(api_key, lat, lon)
    if not result['success']:
        return

    if result['has_warning']:
        warning = result['warning_description']
        message = f'''Next Hour\n {warning}'''
        send_telegram_notification(
            setting.telegram_api_token,
            setting.telegram_chat_id,
            message
        )


def daily_alarms():
    '''
    Sends daily alarm:
    '''

    setting = Setting.objects.first()
    api_key = setting.open_weather_key
    lat = setting.location_latitude
    lon = setting.location_longitude

    result = get_tomorrow_forecast(api_key, lat, lon)
    if not result['success']:
        return

    # check if heat alarm is activated
    if setting.heat_alarm:
        # send telegram notificaitons for heat alarm
        if result['has_heat_warning']:
            temp = result['max_temp']
            message = f'''Tomorrow heat warning, maximum temprature {temp}'''
            send_telegram_notification(
                setting.telegram_api_token,
                setting.telegram_chat_id,
                message
            )

    # check if frost alarm is activated
    if setting.frost_alarm:
        if result['has_frost_warning']:
            temp = result['min_temp']
            message = f'''Tomorrow heat warning, minimum temprature {temp}'''
            send_telegram_notification(
                setting.telegram_api_token,
                setting.telegram_chat_id,
                message
            )
