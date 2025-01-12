from selenium import webdriver
import allure
import pytest
import time

@allure.title("open the app.vwo.com")
@pytest.mark.regression
def test_vwo_login():
    driver = webdriver.Edge()
    driver.get("http:/app.vwo.com")
    time.sleep(15)