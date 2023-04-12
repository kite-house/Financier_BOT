from datetime import datetime
import threading
import time
from DataBase import db

def sys_time():
    while True:
        date_time = datetime.today().replace(microsecond=0)
        if date_time.day == 1 and date_time.hour == 0 and date_time.minute == 0 and date_time.second == 0:
            db.add_new_month_in_db()

        time.sleep(1)

sys_time = threading.Thread(target = sys_time)
sys_time.start()