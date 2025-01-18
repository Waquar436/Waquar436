import pytest
import allure
from selenium import webdriver


@allure.title("verify that the title of katalon-demo-cura is expected")
def test_katalon_edge():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    if "PURA Healthcare Service" in driver.page_source:
        print("Test case passed.")
    else:
        print("Test case failed.")
        pytest.fail("Test not found on the page")




