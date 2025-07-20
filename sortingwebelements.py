import time

from select import select
from selenium import webdriver

from selenium.webdriver.common.by import By



driver.find_element(By.CSS_SELECTOR,"th[aria-sort='descending']").click()
veggie_list=driver.find_elements(By.XPATH,"//tr/td[1]")
newbrowsersortedlist=[]
for veggy in veggie_list:
    newbrowsersortedlist.append(veggy.text)
    print(newbrowsersortedlist)
originalList=newbrowsersortedlist.copy()

print(newbrowsersortedlist)
newbrowsersortedlist.sort()
print(originalList)
assert originalList==newbrowsersortedlist

