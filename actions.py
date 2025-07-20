import time

from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
actions= ActionChains(driver)
