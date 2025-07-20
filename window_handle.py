import time

from select import select
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CSS_SELECTOR,".blinkingText").click()
window_list=driver.window_handles
driver.switch_to.window(window_list[1])
text_on_childwindow=driver.find_element(By.XPATH,"//p[@class='im-para red']").text
username=text_on_childwindow.split()[4]
print(username)
driver.close()
driver.switch_to.window(window_list[0])
driver.find_element(By.ID,"username").send_keys(username)
driver.find_element(By.ID,"password").send_keys("learning")
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,"input[type='checkbox']")))
driver.find_element(By.CSS_SELECTOR,"input[type='checkbox']").click()
driver.find_element(By.ID,"signInBtn").click()
waits=WebDriverWait(driver,10)
waits.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".alert")))
alerts=driver.find_element(By.CSS_SELECTOR,".alert").text
print(alerts)






