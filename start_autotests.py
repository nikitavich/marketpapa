import os

import requests


def start_advertising_autotests():
    message = ''
    result = cons_read(
        mstr="python3 -m pytest --no-header -q --tb=line --disable-warnings tests/backend/test_advertising_cabinet.py")
    if 'ERROR' in result:
        send_message_to_telegram("Тестирование рекламы", 'ERROR в автотестах рекламы')
    if "FAILED" in result:
        cropped_result = result.partition("=\n")
        cropped_result = cropped_result[2].partition("\n=")
        cropped_result = cropped_result[0].split('\n')
        for line in cropped_result:
            exp = line.partition('cabinet.py:')
            message = message + exp[2] + '\n'
        send_message_to_telegram("Тестирование рекламы", message)


def start_internal_analytics_autotests():
    message = ''
    result = cons_read(
        mstr="python3 -m pytest --no-header -q --tb=line --disable-warnings tests/backend/test_internal_analytics.py")
    if 'ERROR' in result:
        send_message_to_telegram("Тестирование внутренней аналитики", 'ERROR в автотестах внутренней аналитики')
    if "FAILED" in result:
        cropped_result = result.partition("\n")
        cropped_result = cropped_result[2].partition("\n=")
        cropped_result = cropped_result[0].split('\n')
        for line in cropped_result:
            exp = line.partition('test_internal_analytics.py:')
            message = message + exp[2] + '\n'
        send_message_to_telegram("Тестирование внутренней аналитики", message)


def start_ui_smoke_autotests():
    message = ''
    result = cons_read(
        mstr="python3 -m pytest --no-header -q --tb=line --disable-warnings tests/smoke/test_smoke.py")
    if 'ERROR' in result:
        send_message_to_telegram("Тестирование UI smoke автотестов", 'ERROR в UI smoke автотестах')
    if "FAILED" in result:
        cropped_result = result.partition("\n")
        cropped_result = cropped_result[2].partition("\n=")
        cropped_result = cropped_result[0].split('\n')
        for line in cropped_result:
            exp = line.partition('test_smoke.py:')
            message = message + exp[2] + '\n'
        send_message_to_telegram("Тестирование UI smoke автотестов", message)

def cons_read(mstr):
    a = os.popen(mstr)
    res = a.read()
    a.close()
    return res


def send_message_to_telegram(part_of_testing: str, message: str):
    url = f"https://api.telegram.org/bot5904586368:AAGeq8gVmaRskgaR6iCcpzmWQa_eZw1y0tQ/sendMessage"
    payload = f'chat_id=-1001899352898&text={part_of_testing}\n{message}'.encode(
        'utf-8')
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    requests.request("POST", url, headers=headers, data=payload)


if __name__ == '__main__':
    start_internal_analytics_autotests()
    start_advertising_autotests()
    start_ui_smoke_autotests()
