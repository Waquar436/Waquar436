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
def test_js_alert_normal():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    element_prompt=driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']")
    element_prompt.click()
    WebDriverWait(driver=driver,timeout=3).until(ec.alert_is_present())
    alert=driver.switch_to.alert
    alert.accept()
    result_text=driver.find_element(By.ID,"result").text
    assert result_text == "You successfully clicked an alert"


def test_js_alert_confirm():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    element_prompt=driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']")
    element_prompt.click()
    WebDriverWait(driver=driver,timeout=3).until(ec.alert_is_present())
    alert=driver.switch_to.alert
    alert.dismiss()
    result_text=driver.find_element(By.ID,"result").text
    assert result_text == "You clicked: Cancel"


def test_js_alert_prompt():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    element_prompt=driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']")
    element_prompt.click()
    WebDriverWait(driver=driver,timeout=3).until(ec.alert_is_present())
    alert=driver.switch_to.alert
    alert.send_keys("waquar")
    alert.accept()
    result_text=driver.find_element(By.ID,"result").text
    assert result_text == "You entered: waquar"
