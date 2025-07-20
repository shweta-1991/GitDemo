import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--browsername", action="store", default="chrome", help="Type in browser name like chrome or firefox")


@pytest.fixture(scope="function")
def browserInstance(request):
    service_obj = Service()
    browsername=request.config.getoption("browsername")
    if browsername=="chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        driver=webdriver.Chrome(service=service_obj, options=options)
        driver.implicitly_wait(4)
    elif browsername=="firefox":
        driver=webdriver.Firefox(service=service_obj)
        driver.implicitly_wait(4)

    yield driver
    driver.close()
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getpluginsmanager('html')
    outcome = yield
    report = outcome.get_result()
    




