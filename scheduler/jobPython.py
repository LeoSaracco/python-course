# To run this proyect you have to excecute "pip install schedule" previously run the app
import schedule
import time

def job():
    print("Reading job")

def jobTimeSet():
    print("Reading job at " + time.asctime(time.localtime()))

# To ten second
schedule.every(10).seconds.do(job)

# To specific time
schedule.every().day.at("16:40").do(jobTimeSet)

while True:
    schedule.run_pending()
    time.sleep(1)
