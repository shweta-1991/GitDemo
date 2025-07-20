from selenium.webdriver.common.by import By


class sorting_elements:
    def __init__(self,driver):
        self.driver=driver
        self.sortclick=(By.CSS_SELECTOR, "th[aria-sort='descending']")
        self.veggies=(By.XPATH, "//tr/td[1]")


    def first_sort(self):
        self.driver.find_element(*self.sortclick).click()

    def second_veggielist(self):
        veggie_list = self.driver.find_elements(*self.veggies)
        newbrowsersortedlist = []
        for veggy in veggie_list:
            newbrowsersortedlist.append(veggy.text)
            print(newbrowsersortedlist)
        originalList = newbrowsersortedlist.copy()

        print(newbrowsersortedlist)
        newbrowsersortedlist.sort()
        print(originalList)
        assert originalList == newbrowsersortedlist