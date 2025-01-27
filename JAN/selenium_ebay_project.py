import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import allure

@allure.title("Print the title of the ebay sites after searching")
@allure.description("verify that 62 items are there for macmini")

def test_ebay():
    print("do it")
