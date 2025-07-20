from selenium.webdriver.common.by import By

from pageObjects.checkout import CheckOut


class Shop:
    def __init__(self, driver):
        self.driver=driver
        self.shop_name=(By.CSS_SELECTOR, " a[href*='shop']")
        self.products_list=(By.XPATH, "//div[@class='card h-100']")
        self.go_to_cartbutton=(By.CSS_SELECTOR, "a[class*='btn-primary']")




    def add_to_cart(self,product_name):
        self.driver.find_element(*self.shop_name).click()
        products = self.driver.find_elements(*self.products_list)

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == product_name:
                product.find_element(By.XPATH, "div/button").click()


    def go_to_cart(self):
        self.driver.find_element(*self.go_to_cartbutton).click()
        check_out=CheckOut(self.driver)
        return check_out