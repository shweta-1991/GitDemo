import json

import pytest
from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.login import Loginpage
from pageObjects.shop import Shop
from window_handle import username
file_path="../data/test_e2eTestFrsmework.json"
with open(file_path) as f:
    test_data = json.load(f)
    test_data_list=test_data["data"]



@pytest.mark.parametrize("testlist_item",test_data_list)
def test_e2e(browserInstance,testlist_item):
    driver=browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    login_page=Loginpage(driver)
    print(login_page.getTiltle())
    shop_page=login_page.login(testlist_item["username"],testlist_item["password"])
    shop_page.add_to_cart(testlist_item["product"])
    check_out=shop_page.go_to_cart()
    check_out.checkingout()
    check_out.confirmation_proceeding("ind")
    check_out.validate_order()




