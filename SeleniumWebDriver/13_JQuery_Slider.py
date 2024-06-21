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

print("Loading URL: " + constants.URL_JQUERY_SLIDER_EX)
driver.get(constants.URL_JQUERY_SLIDER_EX)
print("Website Title: " + driver.title)

left_slider = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/span[1]")
right_slider = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/span[2]")

print("Left Slider Location Before Moving: " + str(left_slider.location))
print("Left Slider Location Before Moving: " + str(left_slider.location['x']))
print("Left Slider Location Before Moving: " + str(left_slider.location['y']))
print("Right Slider Location Before Moving: " + str(right_slider.location))
print("Right Slider Location Before Moving: " + str(right_slider.location['x']))
print("Right Slider Location Before Moving: " + str(right_slider.location['y']))
helper_functions.print_seperator(50)

print("Moving both sliders by 100....")
action_chain = ActionChains(driver)
action_chain.drag_and_drop_by_offset(left_slider, 100, 0).perform()
action_chain.drag_and_drop_by_offset(right_slider, -100, 0).perform()

print("Left Slider Location After Moving: " + str(left_slider.location))
print("Left Slider Location Before Moving: " + str(left_slider.location['x']))
print("Left Slider Location Before Moving: " + str(left_slider.location['y']))
print("Right Slider Location After Moving: " + str(right_slider.location))
print("Right Slider Location Before Moving: " + str(right_slider.location['x']))
print("Right Slider Location Before Moving: " + str(right_slider.location['y']))
helper_functions.print_seperator(50)

time.sleep(1)

driver.close()
driver.quit()
