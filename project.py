from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
file = 0
for i in range(1, 20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=2XY1OKBWIK0FH&sprefix=laptop%2Caps%2C239&ref=nb_sb_noss_1")
    #page = 2 means second page, it is customizable
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    # print(elems)
    #puis-card-container is found by inspecting a specific laptop
    # print(elems.text)
    #First we should scrap HTML, first download pages and scrap the data from it so that we don't miss some data.
    print(f"{len(elems)} items found")
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
            f.write(d)
            file += 1
        # print(elem.text)
    time.sleep(2)
driver.close()


