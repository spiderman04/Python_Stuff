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

print("Loading URL: " + constants.URL_WEBTABLE_STATIC)
driver.get(constants.URL_WEBTABLE_STATIC)
helper_functions.print_seperator(50)

# Static Web Table, parse thru the <table> Tag
table_object = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
row_count = len(table_object)
print("Table row count: " + str(row_count))
print("Header Row: " + driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[1]").text)
helper_functions.print_seperator()

table_object = driver.find_elements(By.XPATH, "//table[@name='BookTable']//th")
column_count = len(table_object)
print("Table column count: " + str(column_count))

# Cycle through the Web Table to get all rows except the Header row
for r in range(2, row_count + 1):
    print("Row Data: " + driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["
                                            + str(r) + "]").text)
    for c in range(1, column_count + 1):
       print("Cell Data:" + driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["
                                                + str(r) + "]/td[" + str(c) + "]").text)
    print("== END ROW ===")


# Dynamic Web Table
# OrangeHRM website not available

time.sleep(3)

# try:
#     assert driver.find_element(By.XPATH, "//div[@class='example']").is_displayed()
#     print("The authentication page title is verified!")
# except AssertionError as err:
#     print("Test user authentication failed!")
# helper_functions.print_seperator()

driver.close()
driver.quit()
