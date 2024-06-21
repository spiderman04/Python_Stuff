import os
import constants
import helper_functions
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException


local_path = os.path.dirname(__file__)
print("Base Name: " + os.path.basename(__file__))
print("Directory Name: " + os.path.dirname(__file__))

# Python will look in SCRIPTS path OR specify absolute path
driver = webdriver.Chrome(executable_path="C:\\WebDrivers\\chromedriver.exe", service_args=None)
# driver.maximize_window()

driver.get(constants.URL_ORANGEHRM)

# APPLICATION Commands
print("Page Title : " + driver.title)
print("Current URL: " + driver.current_url)
print("Page Source: " + driver.page_source)
helper_functions.print_seperator()

# CONDITIONAL commands
print("Text Field is Displayed: " + str(driver.find_element(By.ID, "txtUsername").is_displayed()))
print("Text Field is Enabled: " + str(driver.find_element(By.ID, "txtUsername").is_enabled()))
print("Text Field is Selected: " + str(driver.find_element(By.ID, "txtUsername").is_selected()))

driver.find_element(By.ID, "txtUsername").clear()
driver.find_element(By.ID, "txtUsername").send_keys("test@email.com")
print("Text Field Attribute='value': " + str(driver.find_element(By.ID, "txtUsername").get_attribute('value')))

# BROWSER commands -- see below close() and quit()

# NAVIGATIONAL commands
driver.get(constants.URL_SNAPDEAL)
driver.back()
driver.forward()
driver.refresh()

# WAIT commands - Implicit and Explicit built-in
driver.get(constants.URL_ORANGEHRM)
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
time.sleep(5)  # seconds usign Python library

# set the wait setting for all URL calls from this step forward
driver.implicitly_wait(5)
driver.get(constants.URL_ORANGEHRM)

# wait up to 10 seconds explicitly for an object
element = WebDriverWait(driver, 10, poll_frequency=2,
                        ignored_exceptions=[
                            NoSuchElementException,
                            ElementNotVisibleException,
                            ElementNotSelectableException]
                        ).until(ec.presence_of_element_located((By.LINK_TEXT, "OrangeHRM, Inc")))

driver.close()
driver.quit()
