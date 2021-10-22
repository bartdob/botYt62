import os
import time
from selenium import webdriver
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-usage")

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)

# driver = webdriver.Chrome(executable_path='C:/chromedriver', chrome_options=op) local
counter = 0


@sched.scheduled_job('interval', minutes=12)
def timed_job():
    global counter
    driver.get("https://www.youtube.com/watch?v=kbuDAYF781Y")
    print("DONE")
    counter = counter + 1
    print(counter)


sched.start()
