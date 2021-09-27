import unittest
import weather_utils

TEST_OPENWEATHER_KEY = '8351485f84f81a10488f0714cc1ea20d'
TEST_LATITUDE = '33.9037196'
TEST_LONTITUDE = '73.3784368'


class TestWeatherUtils(unittest.TestCase):

    def test_degToCompass(self):
        self.assertEqual(weather_utils.degToCompass(0), 'N')
        self.assertEqual(weather_utils.degToCompass(90), 'E')
        self.assertEqual(weather_utils.degToCompass(180), 'S')
        self.assertEqual(weather_utils.degToCompass(150), 'SSE')

    def test_get_forecast_data(self):

        self.assertFalse(weather_utils.get_forecast_data("", "", ""))

        self.assertFalse(weather_utils.get_forecast_data(
            TEST_OPENWEATHER_KEY, "", ""))

        self.assertFalse(weather_utils.get_forecast_data(
            TEST_OPENWEATHER_KEY, TEST_LATITUDE, ""))

        # wrong cordinates
        self.assertFalse(weather_utils.get_forecast_data(
            TEST_OPENWEATHER_KEY, "abclat", TEST_LONTITUDE))

        # wrong api key
        self.assertFalse(weather_utils.get_forecast_data(
            "abc api key", TEST_LATITUDE, TEST_LONTITUDE))

        # correct cordinates and api key
        self.assertIsInstance(weather_utils.get_forecast_data(
            TEST_OPENWEATHER_KEY, TEST_LATITUDE, TEST_LONTITUDE), dict)

    def test_get_tomorrow_forecast(self):

        self.assertFalse(weather_utils.get_tomorrow_forecast("", "", ""))

        self.assertFalse(weather_utils.get_tomorrow_forecast(
            TEST_OPENWEATHER_KEY, "", ""))

        self.assertFalse(weather_utils.get_tomorrow_forecast(
            TEST_OPENWEATHER_KEY, TEST_LATITUDE, ""))

        # wrong cordinates
        self.assertFalse(weather_utils.get_tomorrow_forecast(
            TEST_OPENWEATHER_KEY, "abclat", TEST_LONTITUDE))

        # wrong api key
        self.assertFalse(weather_utils.get_tomorrow_forecast(
            "abc api key", TEST_LATITUDE, TEST_LONTITUDE))

        # correct cordinates and api key
        self.assertIsInstance(weather_utils.get_tomorrow_forecast(
            TEST_OPENWEATHER_KEY, TEST_LATITUDE, TEST_LONTITUDE), dict)

    def test_get_next_hour_forecast(self):

        self.assertFalse(weather_utils.get_next_hour_forecast("", "", ""))

        self.assertFalse(weather_utils.get_next_hour_forecast(
            TEST_OPENWEATHER_KEY, "", ""))

        self.assertFalse(weather_utils.get_next_hour_forecast(
            TEST_OPENWEATHER_KEY, TEST_LATITUDE, ""))

        # wrong cordinates
        self.assertFalse(weather_utils.get_next_hour_forecast(
            TEST_OPENWEATHER_KEY, "abclat", TEST_LONTITUDE))

        # wrong api key
        self.assertFalse(weather_utils.get_next_hour_forecast(
            "abc api key", TEST_LATITUDE, TEST_LONTITUDE))

        # correct cordinates and api key
        self.assertIsInstance(weather_utils.get_next_hour_forecast(
            TEST_OPENWEATHER_KEY, TEST_LATITUDE, TEST_LONTITUDE), dict)


if __name__ == "__main__":
    unittest.main()
