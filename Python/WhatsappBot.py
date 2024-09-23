from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

driver.get('https://web.whatsapp.com')
time.sleep(20)

search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/div[2]/div/div[1]/p')
time.sleep(0.5)
search_box.clear()
search_box.send_keys('Darshan')
time.sleep(0.5)
search_box.send_keys(Keys.ENTER)
search_box.send_keys(Keys.ENTER)
