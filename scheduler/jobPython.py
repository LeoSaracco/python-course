# To run this proyect you have to excecute "pip install schedule" previously run the app
import schedule
import time
import requests

def job():
    print("Reading job")

def jobTimeSet():
    print("Reading job at " + time.asctime(time.localtime()))

def getDolarPrice():
    url = "https://api.bluelytics.com.ar/v2/latest"
    page = requests.get(url)
    data = page.json()
    print("Valor dolar:\n", data["blue"])

# To thirty second
schedule.every(30).seconds.do(job)

# To specific time
schedule.every().day.at("16:50").do(jobTimeSet)

# To specific time calling API
schedule.every().day.at("16:51").do(getDolarPrice)

while True:
    schedule.run_pending()
    time.sleep(1)
