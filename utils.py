import pyautogui
import winsound
import subprocess

from datetime import datetime


def try_parse_int(s, var_name):
    try:
        return int(s)
    except ValueError:
        print(f'"{var_name}" needs to be a numeric value')


def try_parse_time(s, time_format, var_name) -> datetime:
    try:
        today = datetime.today()
        temp = datetime.strptime(s, time_format)
        return datetime(year=today.year, month=today.month, day=today.day, hour=temp.hour, minute=temp.minute,
                        second=temp.second)
    except ValueError:
        print(f'"{var_name}" needs to be a valid time')


def shutdown(shutdown_delay, freq, duration):
    print('Beginning shutdown...')
    winsound.Beep(freq, duration)
    winsound.Beep(freq, duration)
    winsound.Beep(freq, duration)

    print(f'Shutting down in {shutdown_delay} seconds...')
    subprocess.call(['shutdown', '-s', '-t', f"{shutdown_delay}"])


def key_press(key):
    if key not in pyautogui.KEY_NAMES:
        raise ValueError(f'Invalid default key: {key}.')
    pyautogui.keyDown(key)
    pyautogui.keyUp(key)
