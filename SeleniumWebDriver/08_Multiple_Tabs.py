import os
import time
import constants
import helper_functions
# import requests   # From Settings/Project Interpreter/requests package

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select

local_path = os.path.dirname(__file__)
print("Base Name: " + os.path.basename(__file__))
print("Directory Name: " + os.path.dirname(__file__))

# Python will look in SCRIPTS path OR specify absolute path
service_object = Service("C:\\WebDrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
print("Loading URL: " + constants.URL_ORANGEHRM)
driver.get(constants.URL_ORANGEHRM)

# Generate window handles are unique IDs:
#   C7B734FCBBC7F60D64BE88C1BD0BDEA9
#   BBFD0BB43B214ADAB55CF1083706D546
window_id = driver.current_window_handle
driver.switch_to.window(window_id)
print("Current Window ID: " + str(window_id))

# open a second tab
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
window_ids = driver.window_handles
for id in window_ids:
    print("\tWindow ID: " + str(id))
helper_functions.print_seperator(60)

driver.switch_to.window(window_ids[1])
print("Child Tab Title: " + driver.title)

driver.switch_to.window(window_ids[0])
print("Parent Tab Title: " + driver.title)

# Close the child window/tab
window_ids = driver.window_handles
for id in window_ids:
    driver.switch_to.window(id)
    print("\tWindow ID: " + str(id) + ", Title: " + driver.title)
    if driver.title == "OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS":
        driver.close()
helper_functions.print_seperator(60)

time.sleep(2)

try:
    driver.get(constants.URL_ORANGEHRM)
    driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
    driver.close()
    driver.quit()
except Exception as exp:
    print("An exception has occurred" + str(exp))

