import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *


@allure.title("Modal")
@allure.description("verify modal")
def test_js_modal():
    driver = webdriver.Chrome()
    driver.get("https://www.makemytrip.com/")
    # element_prompt=driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']")
    # element_prompt.click()
    WebDriverWait(driver=driver, timeout=5).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='commonModal__close'")))
    modal = driver.find_element(By.XPATH, "//span[@class='commonModal__close'")
    modal.click()
