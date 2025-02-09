import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

@allure.title("Spicejet Automation")
@allure.description("Verify spicejet automation using action  classes")
def test_verify_action_Spicejet():
    chrome_options=webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver=webdriver.Chrome(chrome_options)
    driver.get("https://www.spicejet.com/")
    driver.maximize_window()
    # WebDriverWait(driver=driver,timeout=5).until(EC.visibility_of_element_located((By.XPATH,"(//span[@class='commonModal__close'])[1]")))
    # driver.find_element(By.XPATH,"(//span[@class='commonModal__close'])[1]").click()
    # time.sleep(2)
    fromCity=driver.find_element(By.XPATH,"//div[@class='css-1dbjc4n r-1phboty r-1loqt21 r-1qhn6m8 r-1yzf0co r-1otgn73']")
    actions=ActionChains(driver=driver)
    actions.move_to_element(fromCity).click().send_keys("del").perform()
    time.sleep(5)
    # actions.move_to_element(fromCity).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
    # time.sleep(5)
    driver.quit()


