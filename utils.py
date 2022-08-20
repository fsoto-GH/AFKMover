import subprocess, winsound
from datetime import datetime


def try_parse_int(s, var_name):
    try:
        return int(s)
    except ValueError:
        print(f'"{var_name}" needs to be a numeric value')


def try_parse_time(s, format, var_name) -> datetime:
    try:
        today = datetime.today()
        temp = datetime.strptime(s, format)
        return datetime(year=today.year, month=today.month, day=today.day, hour=temp.hour, minute=temp.minute,
                        second=temp.second)
    except  ValueError:
        print(f'"{var_name}" needs to be a valid time')


def shutdown(shutdown_delay, freq, duration):
    print('Beginning shutdown...')
    winsound.Beep(freq, duration)
    winsound.Beep(freq, duration)
    winsound.Beep(freq, duration)

    print(f'Shutting down in {shutdown_delay} seconds...')
    subprocess.call(['shutdown', '-s', '-t', f"{shutdown_delay}"])
