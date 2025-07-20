class BrowserUtils:
    def __init__(self, driver):
        self.driver=driver

    def getTiltle(self):
        return self.driver.title

