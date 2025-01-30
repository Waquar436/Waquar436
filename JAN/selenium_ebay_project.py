import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import allure

@allure.title("Print the title of the ebay sites after searching")
@allure.description("verify that 62 items are there for macmini")

def test_ebay():
    driver=webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    search_box_input_path=driver.find_element(By.XPATH,"//input[@placeholder='Search for anything']")

    search_box_input_path.send_keys("macmini")
    search_btn=driver.find_element(By.CSS_SELECTOR,".gh-search-button__label")
    search_btn.click()
    #//div[@class="s-item__title"] -> s-item__title
    list_of_items=driver.find_elements(By.XPATH,"//div[@class='s-item__title']")
    list_of_item_price=driver.find_elements(By.XPATH,"//span[@class='s-item__price']")
    title_text=[item.text for item in list_of_items]
    price_text=[price.text for price in list_of_item_price]
    for text,price in zip(title_text,price_text):
        print(text,price)
    driver.quit()
    # for items in list_of_items:
    #     print(items.text)
    # for items_prise in list_of_item_price:
    #     print(items_prise.text)



