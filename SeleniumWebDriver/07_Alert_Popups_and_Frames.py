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
print("Loading URL: " + constants.URL_JAVASCRIPT_ALERTS)
driver.get(constants.URL_JAVASCRIPT_ALERTS)

driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(2)
alert_window = driver.switch_to.alert

print(alert_window.text)
alert_window.send_keys("Hello")
alert_window.accept()  # OK button
helper_functions.print_seperator()

# Test the Dismiss button
print("Loading URL: " + constants.URL_JAVASCRIPT_ALERTS)
driver.get(constants.URL_JAVASCRIPT_ALERTS)

driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(2)
alert_window = driver.switch_to.alert

print(alert_window.text)
alert_window.send_keys("Hello")
alert_window.dismiss()  # Cancel button
helper_functions.print_seperator()

# Close an alert popup
print(constants.URL_POPUP_ALERTS)
driver.get(constants.URL_POPUP_ALERTS)

driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(5)
alert_window = driver.switch_to.alert.accept()
helper_functions.print_seperator()

# Authentication Popup
print("Authentication URL: " + constants.URL_AUTH_POPUP)
username = constants.AUTH_POPUP_USERNAME
password = constants.AUTH_POPUP_PASSWORD
url = constants.URL_AUTH_POPUP.replace("https://", "https://" + username + ":" + password + "@")
print("Authentication URL with credentials: " + url)
driver.get(url)

time.sleep(5)

try:
    assert driver.find_element(By.XPATH, "//div[@class='example']").is_displayed()
    print("The authentication page title is verified!")
except AssertionError as err:
    print("Test user authentication failed!")
helper_functions.print_seperator()

# Working with Frames, Iframes, or Forms. Note the context switching to .default_content()
# The method .parent_frame() should work also.
print("Selenium URL Frames Test: " + constants.URL_SELENIUM_DOC_FRAME)
driver.get(constants.URL_SELENIUM_DOC_FRAME)

# Frame 1 - Reference by Name
driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()

# Frame 2 - Reference by Index
driver.switch_to.default_content()
driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT, "WebDriver")

# Frame 3 - Help menu
driver.switch_to.default_content()
driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[8]").click()
helper_functions.print_seperator()

# Inner Frames Example
print("Inner Frames Test: " + constants.URL_INNER_FRAMES)
driver.get(constants.URL_INNER_FRAMES)

# Click on button first to load the inner frame page
driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()
outer_frame = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outer_frame)

# Locate the inner frame and change context, then enter text
inner_frame = driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
driver.switch_to.frame(inner_frame)
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Welcome!")
driver.switch_to.parent_frame()
helper_functions.print_seperator()

driver.close()
driver.quit()
