import time
import dotenv
import os
from datetime import datetime
import subprocess


dotenv.load_dotenv()

times = os.getenv("TIME").split(',')


formatted_date = []
for t in times:
    t_obj = datetime.strptime(t, "%H:%M").time()
    formatted_date.append(t_obj)

# Sort the times
formatted_date.sort()

# Process the queue
while formatted_date:
    qtime = formatted_date.pop(0)
    current_time = datetime.now().time()

    # Convert both times to seconds
    qtime_seconds = qtime.hour * 3600 + qtime.minute * 60 + qtime.second
    current_seconds = current_time.hour * 3600 + current_time.minute * 60 + current_time.second

    if current_seconds > qtime_seconds:
        continue  # Skip past times
    else:
        delay = qtime_seconds - current_seconds
        time.sleep(delay)
        try:
            subprocess.run(["pythonw", f"{os.getenv('ABS_PATH')}\\college_assignments"], check=True)
        except Exception as ex:
            pass