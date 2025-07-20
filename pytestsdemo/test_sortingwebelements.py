import time

import pytest
from select import select
from selenium import webdriver

from selenium.webdriver.common.by import By

from pageObjects.sorting_elements import sorting_elements

@pytest.mark.smoketest
def test_sortingwebelements(browserInstance):
    driver=browserInstance
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    sorting_elem=sorting_elements(driver)
    sorting_elem.first_sort()
    sorting_elem.second_veggielist()





