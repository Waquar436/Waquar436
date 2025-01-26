import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *

@allure.title("Alerts")
@allure.description("verify alerts")
def test_js_alerts():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    element_prompt=driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']")
    element_prompt.click()
    WebDriverWait(driver=driver,timeout=3).until(ec.alert_is_present())
    alert=driver.switch_to.alert
    alert.accept()
