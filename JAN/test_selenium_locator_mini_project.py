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
@pytest.mark.negativevwologin
def test_app_vwo_login_chrome():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("URL"))
    # type = "email"
    # class ="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi"
    email_web_element = driver.find_element(By.ID, value="login-username")
    email_web_element.send_keys(os.getenv("INVALID_USER"))
    # class ="text-input W(100%)"
    # name="password"
    # id="login-password"
    # data-qa="jobodapuxe"
    pwd_web_element = driver.find_element(By.ID, value="login-password")
    pwd_web_element.send_keys((os.getenv("INVALID_PWD")))
    #     < button
    #     type = "submit"
    #     id = "js-login-btn"
    #
    #     class ="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)" onclick="login.login(event)" data-qa="sibequkica" >
    #
    #     < span
    #
    #     class ="icon loader hidden" data-qa="zuyezasugu" > < / span >
    #
    #     < span
    #     data - qa = "ezazsuguuy" > Sign in < / span >
    #
    # < / button >
    submit_btn_web_element = driver.find_element(By.ID, value="js-login-btn")
    submit_btn_web_element.click()
    time.sleep(3)
    # class ="notification-box-description"
    # id="js-notification-box-msg"
    # data-qa="rixawilomi"
    error_msg_web_element = driver.find_element(By.ID, value="js-notification-box-msg")
    assert error_msg_web_element.text == os.getenv("error_msg_expected")
