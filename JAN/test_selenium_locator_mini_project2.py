import pytest
import allure
import time
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os


@allure.title("VWO Login Negative Testcase")
@allure.description("TC1 - Negative TC - VWO Login with invalid creds")
def test_app_vwo_login_chrome():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("URL"))
    # < a
    # href = "https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page&amp;utm_campaign=mof_eg_loginpage"
    # class ="text-link"
    # data-qa="bericafeqo" > Start a free trial < / a >
    all_links_pages = driver.find_elements(By.TAG_NAME,value="a")
    for i in all_links_pages:
        # print(i.text)
        if "Start a free trial" in i.text:
            i.click()
    time.sleep(3)
    driver.quit()