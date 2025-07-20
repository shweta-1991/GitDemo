from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CheckOut:

    def __init__(self, driver):
        self.driver = driver
        self.checkbutton = (By.XPATH, "//button[@class='btn btn-success']")
        self.country_click = (By.ID, "country")
        self.final_button = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.final_submit = (By.CSS_SELECTOR, "[type='submit']")
        self.country_input = (By.LINK_TEXT, "India")
        self.message = (By.CLASS_NAME, "alert-success")

    def checkingout(self):
        self.driver.find_element(*self.checkbutton).click()

    def confirmation_proceeding(self, country):

        self.driver.find_element(*self.country_click).send_keys(country)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.country_input))
        self.driver.find_element(*self.country_input).click()
        self.driver.find_element(*self.final_button).click()
        self.driver.find_element(*self.final_submit).click()

    def validate_order(self):
        successText = self.driver.find_element(*self.message).text
        assert "Success! Thank you!" in successText
