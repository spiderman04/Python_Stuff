import os
import time
import constants
import helper_functions

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

local_path = os.path.dirname(__file__)
print("Base Name: " + os.path.basename(__file__))
print("Directory Name: " + os.path.dirname(__file__))

# Override the Chrome Options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--start-fullscreen")
chrome_options.add_argument("--disable-popup-blocking")

# Python will look in SCRIPTS path OR specify absolute path
service_object = Service("C:\\WebDrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_object, options=chrome_options)

print("Loading URL: " + constants.URL_POPUP_WHAT_MY_LOCATION)
driver.get(constants.URL_POPUP_WHAT_MY_LOCATION)
driver.maximize_window()
helper_functions.print_seperator()

time.sleep(3)

driver.close()
driver.quit()
