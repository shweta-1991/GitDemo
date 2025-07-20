import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#ser_obj=Service("")
#driver=webdriver.Chrome(service=ser_obj)
driver=webdriver.Chrome()
driver.implicitly_wait(10)
#time.sleep(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(10)
expectedlist=['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
new_cart=driver.find_elements(By.XPATH,"//h4[@class='product-name']")
newlist=[]
for cart in new_cart:
    print(cart.text)
    newlist.append(cart.text)
print(newlist)

assert newlist==expectedlist
res= driver.find_elements(By.XPATH,"//button[text()='ADD TO CART']")
print(len(res))
for res1 in res:
    print(res1.text)
    res1.click()
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

amounts=driver.find_elements(By.CSS_SELECTOR,'tr td:nth-child(5) p')
sum=0
for amount in amounts:
    sum = sum+ int(amount.text)

assert sum==int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
print(sum)
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)

totalamount=int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
discountedamount= float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
print(totalamount)
print(discountedamount)
assert totalamount>discountedamount
driver.find_element(By.XPATH,"//button[text()='Place Order']").click()

