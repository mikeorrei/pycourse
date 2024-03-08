from datetime import datetime, timedelta
import time

delta = timedelta(minutes=1)
current = datetime.now()
target = current + delta

while True:
    current = datetime.now()
    print(f"Current time is {current}, target time is {target}")

    if current >= target:
        break

    time.sleep(5)