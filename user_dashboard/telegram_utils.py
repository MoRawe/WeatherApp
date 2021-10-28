import requests


def send_telegram_notification(api_key, chat_id, text):
    '''
    Send message to on telegram app using api key and chat ID

    @params
    api_key - telegram app key
    chat_id - user chat ID
    text - message that will be sent
    '''
    try:
        url = 'https://api.telegram.org/bot' + api_key + \
            '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + text
        res = requests.get(url).json()
        if not res['ok']:
            return False

        return True

    except:
        return False


def send_test_notification(api_key, chat_id):
    text = '''
    🔔 Testing 🔔

Congrats! your telegram bot is working perfectly. ✅
    '''

    return send_telegram_notification(api_key, chat_id, text)


if __name__ == "__main__":
    send_test_notification(
        "1994210288:AAFGiJ-WXL8yrRR3a1siyWTowuMrepBV1B4", '1372913634')
