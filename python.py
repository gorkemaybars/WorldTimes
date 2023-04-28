import datetime
import pytz
from colorama import init, Fore, Style
import time


init()

timezones = {
    'New York': 'America/New_York',
    'London': 'Europe/London',
    'Paris': 'Europe/Paris',
    'Moscow': 'Europe/Moscow',
    'Dubai': 'Asia/Dubai',
    'Tokyo': 'Asia/Tokyo',
    'Sydney': 'Australia/Sydney',
    'Turkey': 'Europe/Istanbul'
}


while True:
    for city, timezone in timezones.items():
        tz = pytz.timezone(timezone)
        current_time = datetime.datetime.now(tz)
        if current_time.hour >= 6 and current_time.hour < 12:
            color = Fore.YELLOW
        elif current_time.hour >= 12 and current_time.hour < 18:
            color = Fore.GREEN
        else:
            color = Fore.BLUE
        print(f"{color}{city}: {current_time.strftime('%H:%M:%S')} {Style.RESET_ALL}", end='\t')
    print('\n')
    time.sleep(1)
