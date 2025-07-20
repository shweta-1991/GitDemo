import time

from select import select
from selenium import webdriver

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

time.sleep(5)
driver.find_element(By.ID,"name").send_keys("shweta")
driver.find_element(By.ID,"alertbtn").click()

alertpop = driver.switch_to.alert
print(alertpop.text)
alertpop.accept()


#driver.find_element(By.CSS_SELECTOR, "label[for='fromCity'] span[class='lbl_input appendBottom10']").send_keys("Ind")
##dropdown=driver.find_elements(By.CSS_SELECTOR,"span.lbl_input")
#print(len(dropdown))
#print(dropdown)
#for elem in  dropdown:
    #if elem.text=="Indore":
       # elem.click()
      #  print(elem.text)
       # break
  ##  assert elem.is_selected()

        


