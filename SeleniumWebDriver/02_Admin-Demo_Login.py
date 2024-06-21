import os
import constants
import helper_functions

from selenium import webdriver
from selenium.webdriver.common.by import By

local_path = os.path.dirname(__file__)
print("Base Name: " + os.path.basename(__file__))
print("Directory Name: " + os.path.dirname(__file__))

# Python will look in SCRIPTS path OR specify absolute path
driver = webdriver.Chrome(executable_path="C:\\WebDrivers\\chromedriver.exe", service_args=None)
# driver.maximize_window()

driver.get(constants.URL_ADMIN_DEMO)
assert driver.title == 'Your store. Login'
helper_functions.count_links(driver)

driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID, 'Password').clear()
driver.find_element(By.ID, 'Password').send_keys('admin')
driver.find_element(By.CSS_SELECTOR, '.button-1').click()
helper_functions.count_links(driver)

try:
    assert driver.title == 'Dashboard / nopCommerce administration'
    print("The page title is verified!")
except AssertionError as err:
    print("The page TITLE does not match 'Dashboard / nopCommerce administration'")

driver.close()
driver.quit()
