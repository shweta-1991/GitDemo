from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.shop import Shop
from util.browserutils import BrowserUtils
from window_handle import username


class Loginpage(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.signin_button = (By.ID, "signInBtn")
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.signin_button).click()
        shop_page = Shop(self.driver)
        return shop_page
