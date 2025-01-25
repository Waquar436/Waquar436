from selenium import webdriver
from selenium.webdriver.common.by import By
def test_dynamicwebtables():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable1.html")
    table=driver.find_element(By.XPATH,"//table[@Summary='Sample Table']/tbody")
    row_table=table.find_elements(By.TAG_NAME,"tr")
    for row in row_table:
        cols=row.find_elements(By.TAG_NAME,"td")
        for e in cols:
            print(e.text)
