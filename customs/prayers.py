import requests
import json
import datetime
import time


def flash_text(text, times=5):
  for _ in range(times):
    # print('\033[5;31;40m' + text + '\033[0m', end='\r')
    print(text)
    time.sleep(0.5)
    print(' ' * (len(text) + 10))
    # print(' ' * (len(text) + 10), end='\r')
    time.sleep(0.5)


response = requests.get('https://api.aladhan.com/v1/timingsByCity?city=Saint-Chamas&country=France&method=12')

content = json.loads(response.content)
current_time = datetime.datetime.now()

current_hour = current_time.strftime("%H:%M")
next_prayer_time = None

for time_items in content['data']['timings'].items():  
  if 'Sunrise' in time_items or 'Sunset' in time_items:
    continue

  if time_items[1] > current_hour:
    next_prayer_time = ' '.join(time_items)
    break


print(f"🕌 {next_prayer_time}")

# flash_text(next_prayer_time, times=5)
# print(flash_text(f"🕌 {next_prayer_time}", times=5))
# flash_text("Flashing Text", times=5)
