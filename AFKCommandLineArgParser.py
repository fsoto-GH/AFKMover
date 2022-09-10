import pyautogui

from utils import try_parse_int, try_parse_time

DF_SLEEP_TIME = 3
DF_TIME_FORMAT = '%I:%M:%S%p'
DF_KEY_TO_PRESS = 'win'

SLEEP_TIME_CODE = 'st'
STOP_TIME_CODE = 'tm'
SHUTDOWN_DELAY_CODE = 'sd'
KEY_TO_PRESS_CODE = 'kp'

VAR_NAMES = {
    SLEEP_TIME_CODE: 'sleep time',
    STOP_TIME_CODE: 'stop time',
    SHUTDOWN_DELAY_CODE: 'shutdown time',
    KEY_TO_PRESS_CODE: 'key to press'
}

DF_ARGS = {
    SLEEP_TIME_CODE: DF_SLEEP_TIME,
    KEY_TO_PRESS_CODE: DF_KEY_TO_PRESS
}

INVALID_SLEEP_TIME = 'Interval between key presses must be a positive integer.'
INVALID_KEY_PRESS = 'The key selected is not a valid key to press.'
MISSING_SHUTDOWN_FOR_DELAY = 'A stop time must be specified when a shutdown time is specified.'


class AFKCommandLineArgParser:
    def __init__(self, args=None) -> None:
        if args is None:
            self._args = DF_ARGS
        else:
            self.args = args

    @property
    def args(self) -> dict:
        return self._args

    @args.setter
    def args(self, val) -> None:
        res = {}
        for pos_pair in val:
            if '=' in pos_pair:
                key, value = pos_pair.split('=')

                if key in (SLEEP_TIME_CODE, SHUTDOWN_DELAY_CODE):
                    res[key] = try_parse_int(value, VAR_NAMES[key])
                elif key == STOP_TIME_CODE:
                    res[key] = try_parse_time(
                        value, DF_TIME_FORMAT, VAR_NAMES[key])
                elif key == KEY_TO_PRESS_CODE:
                    res[key] = value.lower()
            else:
                raise KeyError(f'Invalid key "{pos_pair}".')

        if SLEEP_TIME_CODE not in res:
            res[SLEEP_TIME_CODE] = DF_SLEEP_TIME

        if KEY_TO_PRESS_CODE not in res:
            res[KEY_TO_PRESS_CODE] = DF_KEY_TO_PRESS

        self._args = res

    def is_valid(self) -> bool:
        is_valid = True

        # if any parsing failed while assigning, then the entry should be None
        # if any value is none, we know something is not right
        if any(v is None for v in self.args.values()):
            is_valid = False

        if SHUTDOWN_DELAY_CODE in self.args and STOP_TIME_CODE not in self.args:
            print(MISSING_SHUTDOWN_FOR_DELAY)
            is_valid = False

        if SLEEP_TIME_CODE in self.args and not self.args[SLEEP_TIME_CODE] > 0:
            print(INVALID_SLEEP_TIME)
            is_valid = False

        if not self._args[KEY_TO_PRESS_CODE] in pyautogui.KEY_NAMES:
            print(INVALID_KEY_PRESS)
            is_valid = False

        return is_valid
