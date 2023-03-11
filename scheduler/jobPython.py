# To run this proyect you have to excecute "pip install schedule" previously run the app
import schedule
import time

def job():
    print("Reading job")

# To every second
schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
