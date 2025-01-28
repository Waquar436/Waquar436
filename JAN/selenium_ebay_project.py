import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import allure

@allure.title("Print the title of the ebay sites after searching")
@allure.description("verify that 62 items are there for macmini")

def test_ebay():
    driver=webdriver.Chrome()
    driver.get("https://www.ebay.com/sch/i.html?_nkw=macmini&_sacat=0&_from=R40&_trksid=p4432023.m570.l1313")
    search_box_input_path=driver.find_element(By.XPATH,"//input[@placeholder='Search for anything']")
    search_box_input_path.send_keys("macmini")
    search_btn=driver.find_element(By.CSS_SELECTOR,"#gh-search-btn > span")


