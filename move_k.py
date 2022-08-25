import sys

from AFKMover import AFKMover
from AFKCommandLineArgParser import AFKCommandLineArgParser
from AFKCommandLineArgParser import SLEEP_TIME_CODE, STOP_TIME_CODE, SHUTDOWN_DELAY_CODE, KEY_TO_PRESS_CODE

HELP_KEYWORDS = ('--help', '--h', 'help')

if __name__ == '__main__':
    args = sys.argv[1:]

    # if there are args, then assert first is not for help
    if len(args) == 0 or len(args) > 0 and not args[0] in HELP_KEYWORDS:
        try:
            commandLineArgs = AFKCommandLineArgParser(args if args else None)

            p = AFKMover(commandLineArgs)
            p.start()
        except (ValueError, KeyError) as ex:
            print(ex)
    else:
        print(f"py move_k.py [[{SLEEP_TIME_CODE}=sleep_time] [{STOP_TIME_CODE}=hh:mm:ss{{AM|PM}}]]"
              f" [{SHUTDOWN_DELAY_CODE}=seconds] [kp={KEY_TO_PRESS_CODE}]]")
