import os
import time
import constants
import helper_functions

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException

local_path = os.path.dirname(__file__)
print("Base Name: " + os.path.basename(__file__))
print("Directory Name: " + os.path.dirname(__file__))

# Chrome
print("Loading URL: " + constants.URL_FILE_DOWNLOAD_EXAMPLES)
driver = helper_functions.setup_chrome()
driver.get(constants.URL_FILE_DOWNLOAD_EXAMPLES)

print("Website Title: " + driver.title)
print("Scrolling by 500 'Y' pixels....")
driver.execute_script("window.scrollBy(0,500)", "")
helper_functions.print_seperator(50)
driver.find_element(By.XPATH, "//*[@id='table-files']/tbody/tr[1]/td[5]/a").click()

# close the popup to complete the download
# Waiting for the element to be clickable with Explicit wait
# wait up to 5 seconds explicitly for an object
# element = WebDriverWait(driver, 5, poll_frequency=2,
#                         ignored_exceptions=[
#                             NoSuchElementException,
#                             ElementNotVisibleException,
#                             ElementNotSelectableException]
#                         ).until(ec.presence_of_element_located((By.XPATH, "//*[@id='dismiss-button']")))

# driver.find_element(By.XPATH,"//*[@id='dismiss-button']").click()

# Edge
# print("Loading URL: " + constants.URL_FILE_DOWNLOAD_EXAMPLES)
# driver = helper_functions.setup_edge()
# driver.get(constants.URL_FILE_DOWNLOAD_EXAMPLES)
#
# print("Website Title: " + driver.title)
# print("Scrolling by 200 'Y' pixels....")
# driver.execute_script("window.scrollBy(0,200)", "")
# helper_functions.print_seperator(50)
# time.sleep(2)
# driver.find_element(By.XPATH, "//*[@id='table-files']/tbody/tr[1]/td[5]/a").click()

# Firefox
# print("Loading URL: " + constants.URL_FILE_DOWNLOAD_EXAMPLES)
# driver = helper_functions.setup_firefox()
# driver.get(constants.URL_FILE_DOWNLOAD_EXAMPLES)
#
# print("Website Title: " + driver.title)
# print("Scrolling by 200 'Y' pixels....")
# driver.execute_script("window.scrollBy(0,200)", "")
# helper_functions.print_seperator(50)
# time.sleep(2)
# driver.find_element(By.XPATH, "//*[@id='table-files']/tbody/tr[1]/td[5]/a").click()

time.sleep(2)

driver.close()
driver.quit()
