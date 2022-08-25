import winsound
from datetime import datetime

from utils import shutdown, key_press
from AFKCommandLineArgParser import AFKCommandLineArgParser
from AFKCommandLineArgParser import STOP_TIME_CODE, SLEEP_TIME_CODE, SHUTDOWN_DELAY_CODE, KEY_TO_PRESS_CODE
from AFKCommandLineArgParser import DF_TIME_FORMAT

INVALID_AFK_CL_ARGS = 'One or more arguments were invalid. Please review the errors above.'


class AFKMover:
    def __init__(self, args: AFKCommandLineArgParser) -> None:
        if not args.is_valid():
            raise ValueError(INVALID_AFK_CL_ARGS)
        self.parser = args

    # method loops until time condition is met
    def start(self):
        if do_stop := STOP_TIME_CODE in self.parser.args:
            print(f'Stopping at {self.parser.args[STOP_TIME_CODE]:{DF_TIME_FORMAT}}.')

        if SHUTDOWN_DELAY_CODE in self.parser.args:
            print(f'Shutting down computer {self.parser.args[SHUTDOWN_DELAY_CODE]} seconds after'
                  f' {self.parser.args[STOP_TIME_CODE]:{DF_TIME_FORMAT}}.')

        last_triggered = datetime.now()
        while True:
            if do_stop and datetime.now() > self.parser.args[STOP_TIME_CODE]:
                print('Stopping as per requested.')
                break

            if (datetime.now() - last_triggered).seconds > self.parser.args[SLEEP_TIME_CODE]:
                key_press(self.parser.args[KEY_TO_PRESS_CODE])
                last_triggered = datetime.now()

        if SHUTDOWN_DELAY_CODE in self.parser.args:
            shutdown(self.parser.args[SHUTDOWN_DELAY_CODE], 1000, 350)
        else:
            winsound.Beep(1000, 1000)
