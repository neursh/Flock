import ntplib, win32api, time
from datetime import datetime, timezone

def setTime():
    response = ntplib.NTPClient().request("time.google.com", version=3)
    time_update = datetime.fromtimestamp(response.tx_time, timezone.utc)
    time_tuple = (time_update.year, time_update.month, time_update.day, time_update.hour, time_update.minute, time_update.second, time_update.microsecond // 1000)

    win32api.SetSystemTime(*(time_tuple[:2] + (datetime(*time_tuple).isocalendar()[2],) + time_tuple[2:]))

tries = 20
while tries:
    try: setTime()
    except: pass
    else: break
    time.sleep(5)
    tries -= 1