prece = input("Ievadiet preci:")
name = []
links = []

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://www.1a.lv"
driver.get(url)
time.sleep(2)

find = driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
find.click()

find = driver.find_element(By.ID, "q")
find.send_keys(prece)
time.sleep(2)

find = driver.find_element(By.CLASS_NAME, "main-search-submit")
find.click()
time.sleep(2)

find = driver.find_element(By.CLASS_NAME, "select2-selection__rendered")
find.click()
time.sleep(2)

find = driver.find_element(By.XPATH, "//li[text()='Cenas, sākot no zemākās']")
find.click()
time.sleep(2)

nosaukums = driver.find_elements(By.CLASS_NAME, "ks-new-product-name")

for nosauk in nosaukums:
    n = nosauk.text
    name.append(n)
    if prece in n:
        link = nosauk.find_element(By.XPATH, ".//ancestor::a").get_attribute("href")
        links.append(link)
if not links:
    print("Prece nav atrasta")
else:
    print('Rekur visizdevigakas preces:')
    
    for i, (product_name, product_link) in enumerate(zip(name, links), 1):
        time.sleep(1)
        print(f'{i}.  Saite: {product_link}\n')

for link in links:
    driver.get(link)
