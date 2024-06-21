import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

local_path = os.path.dirname(__file__)

print("Base Name: " + os.path.basename(__file__))
print("Directory Name: " + os.path.dirname(__file__))

browser = webdriver.Chrome()
browser.get('https://selenium.dev/')

time.sleep(3)

browser.close()