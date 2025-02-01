import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.keys import Keys

@allure.title("Action P1")
@allure.description("Verify Action P1")
def test_verify_action_keyboard():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    #draggable
    element_to_hold=driver.find_element(By.ID,"draggable")
    actions=ActionChains(driver)
    actions.click_and_hold(on_element=element_to_hold).perform()
    time.sleep(10)
    driver.quit()

