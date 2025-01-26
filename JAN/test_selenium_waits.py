import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

@allure.title("app.vwo.com implicit wait")
@allure.description("verify that app.vwo.com is loaded with waits")
def test_negative_app_vwo_com():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    # driver.implicitly_wait(5) #we never use this
    email_web_element=driver.find_element(By.ID,"login-username")
    email_web_element.send_keys("abc@gmail.com")

    password_web_element=driver.find_element(By.NAME,"password")
    password_web_element.send_keys("12345")

    submit_btn_web_element=driver.find_element(By.ID,"js-login-btn")
    submit_btn_web_element.click()

    WebDriverWait(driver,timeout=3).until(ec.visibility_of_element_located((By.CLASS_NAME, "notification-box-description")))
    error_msg_web_element=driver.find_element(By.CLASS_NAME,"notification-box-description")
    print(error_msg_web_element.text)
    assert error_msg_web_element == "your email,password,IP address or location did not match."



