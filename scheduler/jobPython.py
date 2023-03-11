import schedule
import time

def job():
    print("Reading job")

schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
