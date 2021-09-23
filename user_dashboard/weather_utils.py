'''
Utilities for all weather functionality
'''

import requests
import math



def degToCompass(degree):
    val = int((degree/22.5)+.5)
    arr = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
           "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    return arr[(val % 16)]

def get_forecast_data(open_weather_key, lat, lon):
    

    if not open_weather_key:
        return False

    if not lat:
        return False

    if not lon:
        return False

    # call openweather api
    url = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}'.format(
        lat, lon, open_weather_key)
    r = requests.get(url)

    if r.status_code == 400:
        # invalid parameters - i.e lat and lon
        return False

    if r.status_code == 401:
        # invalid api key
        return False

    if r.status_code != 200:
        # openweather server internal errors
        print('openweather: unknown error, code: {}'.format(r.status_code))
        return False

    # start calculations
    json_response = r.json()
    daily_data = json_response['daily'][1:]

    # calculate minimum temprature
    min_temps = []
    for d in daily_data:
        min_temps.append(d['temp']['min'])

    minimum_temprature = min(min_temps)
    # convert kelvin to cel
    minimum_temprature = math.floor(minimum_temprature - 273.15)

    # calculate maximum temprature
    max_temps = []
    for d in daily_data:
        max_temps.append(d['temp']['max'])

    maximum_temprature = max(max_temps)
    # convert kelvin to cel
    maximum_temprature = math.floor(maximum_temprature - 273.15)

    # get winds speed for 7 days (converting mps to kph)
    wind_speeds = []
    for d in daily_data:
        wind_speed_kph = round((3.6 * d['wind_speed']))
        wind_speeds.append(wind_speed_kph)

    # get wind directions for 7 days
    wind_directions = []
    for d in daily_data:
        wind_direction = degToCompass(
            d['wind_deg']) + "  " + str(d['wind_deg'])
        wind_directions.append(wind_direction)

    return {
        'min_temp': minimum_temprature,
        'max_temp': maximum_temprature,
        'wind_speeds': wind_speeds,
        'wind_directions': wind_directions,
    }