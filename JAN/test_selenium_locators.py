import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def test_katalon_chrome():
    chrome_options = Options()
    # chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--window-size=900,600")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment_element = driver.find_element(By.ID,value="btn-make-appointment")
    make_appointment_element.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(10)
    driver.quit()

