import os
import time
import constants
import helper_functions
# import requests   # From Settings/Project Interpreter/requests package

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

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
driver = webdriver.Chrome(service=service_object)
driver.implicitly_wait(10)

# print("Loading URL: " + constants.URL_ORANGEHRM)
# driver.get(constants.URL_ORANGEHRM)
# print("Website Title: " + driver.title)

# driver.find_element(By.ID, "txtUsername").clear()
# driver.find_element(By.ID, "txtUsername").send_keys("Admin")
# driver.find_element(By.ID, 'txtPassword').send_keys('admin123')
# driver.find_element(By.ID, 'btnLogin').click()
# helper_functions.print_seperator(50)

# Mouse hover, define the elements up front!
# menu_admin = driver.find_element(By.XPATH, "//*[@id='menu_admin_viewAdminModule']/b")
# menu_user_management = driver.find_element(By.XPATH, "//*[@id='menu_admin_UserManagement']")
# menu_users = driver.find_element(By.XPATH, "//*[@id='menu_admin_viewSystemUsers']")

# perform the menu selections in sequence
# action_chain = ActionChains(driver)
# action_chain.move_to_element(menu_admin).move_to_element(menu_user_management).move_to_element(menu_users).click()
# action_chain.perform()
# time.sleep(5)

# Right click
# menu_admin = driver.find_element(By.XPATH, "//*[@id='menu_admin_viewAdminModule']/b")
# action_chain = ActionChains(driver)
# action_chain.context_click(menu_admin)
# action_chain.perform()

# Double click
# button = driver.find_element(By.XPATH, "//input[@id='searchBtn']")
# action_chain = ActionChains(driver)
# action_chain.double_click(button)
# action_chain.perform()

# Drag-and-drop
# print("Loading URL: " + constants.URL_DRAG_AND_DROP_DEMO)
# driver.get(constants.URL_DRAG_AND_DROP_DEMO)
# driver.maximize_window()
# print("Website Title: " + driver.title)
# drag_from_obj =  driver.find_element(By.XPATH, "//div[contains(text(), 'Rome')]")
# drag_to_obj = driver.find_element(By.XPATH, "//div[contains(text(), 'Italy')]")
#
# action_chain = ActionChains(driver)
# action_chain.drag_and_drop(drag_from_obj, drag_to_obj).perform()

time.sleep(1)

driver.close()
driver.quit()
