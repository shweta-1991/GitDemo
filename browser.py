import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service

ser_ob = Service(r"C:\Users\SHWETA\Downloads\edgedriver_win64\msedgedriver.exe")

driver = webdriver.Edge(service=ser_ob)
driver.get("http://www.makemytrip.com")
#maximize window
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(5)
