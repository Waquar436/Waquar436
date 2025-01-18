import pytest
import allure
from selenium import webdriver


@allure.title("verify that the content of katalon-demo-cura is expected on multiple browser")
def test_katalon_chrome():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    if "CURA Healthcare Service" in driver.page_source:
        print("Test case passed.")
    else:
        print("Test case failed.")
        pytest.fail("Test not found on the page")

def test_katalon_edge():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    if "CURA Healthcare Service" in driver.page_source:
        print("Test case passed.")
    else:
        print("Test case failed.")
        pytest.fail("Test not found on the page")

def test_katalon_firefox():
    driver = webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    if "CURA Healthcare Service" in driver.page_source:
        print("Test case passed.")
    else:
        print("Test case failed.")
        pytest.fail("Test not found on the page")



