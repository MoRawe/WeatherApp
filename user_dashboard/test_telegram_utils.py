import unittest
import telegram_utils

TELEGRAM_TEST_API_TOKEN = "1994210288:AAFGiJ-WXL8yrRR3a1siyWTowuMrepBV1B4"
TELEGRAM_TEST_CHAT_ID = "1372913634"


class TestTelegramUtils(unittest.TestCase):

    def test_send_notification(self):

        self.assertEqual(
            telegram_utils.send_telegram_notification("", "", ""), False)

        self.assertEqual(
            telegram_utils.send_telegram_notification(TELEGRAM_TEST_API_TOKEN, TELEGRAM_TEST_CHAT_ID, "Test message"), True)

    def test_send_test_notification(self):

        self.assertEqual(
            telegram_utils.send_test_notification("", ""), False)

        self.assertEqual(
            telegram_utils.send_test_notification(TELEGRAM_TEST_API_TOKEN, TELEGRAM_TEST_CHAT_ID), True)


if __name__ == '__main__':
    unittest.main()
