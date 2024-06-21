import os
import time
import constants
import helper_functions


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

print("Loading URL: " + constants.URL_COUNTRIES_OF_THE_WORLD)
driver.get(constants.URL_COUNTRIES_OF_THE_WORLD)
print("Website Title: " + driver.title)
helper_functions.print_seperator(50)

print("Scrolling by 1000 'y' pixels....")
driver.execute_script("window.scrollBy(0,1000)", "")
scroll_value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels move: " + str(scroll_value))
helper_functions.print_seperator(50)

# print("Scrolling object into view....")
# driver.get(constants.URL_COUNTRIES_OF_THE_WORLD)
# driver.execute_script("window.scrollBy(0,5500)", "")
# flag_element = driver.find_element(By.XPATH, "//img[@alt='Flag of United States of America']")
# driver.execute_script(("arguments[0].scrollIntoView();", flag_element))
# scroll_value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixels move: " + str(scroll_value))

print("Scrolling to end of page....")
driver.get(constants.URL_COUNTRIES_OF_THE_WORLD)
scroll_value = driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
scroll_value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels move: " + str(scroll_value))

time.sleep(5)

print("Scrolling to top of page....")
driver.get(constants.URL_COUNTRIES_OF_THE_WORLD)
scroll_value = driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
scroll_value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels move: " + str(scroll_value))

time.sleep(2)

driver.close()
driver.quit()
