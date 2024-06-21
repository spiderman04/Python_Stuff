import os
import time
import constants
import helper_functions


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver import ActionChains

local_path = os.path.dirname(__file__)
print("Base Name: " + os.path.basename(__file__))
print("Directory Name: " + os.path.dirname(__file__))

# Override the Chrome Options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--start-fullscreen")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-plugins")


# Python will look in SCRIPTS path OR specify absolute path
service_object = Service("C:\\WebDrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
driver.implicitly_wait(20)

print("Loading URL: " + constants.URL_TEXT_COMPARE)
driver.get(constants.URL_TEXT_COMPARE)
print("Website Title: " + driver.title)
helper_functions.print_seperator(50)

print("Text Compare Example via Ctrl+A, Ctrl+C, Tab, and Ctrl+V")
# Ctrl+A
driver.find_element(By.ID, "inputText1").clear()
driver.find_element(By.ID, "inputText1").send_keys("abcdefghijklmnopqrstuvqxyz")
print("Entered Text....")
time.sleep(5)

action_chain = ActionChains(driver)
action_chain.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
action_chain.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
print("Copied Text....")

# Tab to the second control
action_chain.send_keys(Keys.TAB).perform()
action_chain.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(5)
print("Pasted Text....")

# Click Compare button to accept the pasted text
driver.find_element(By.XPATH, "//button[@id='compareButton']").click()
time.sleep(5)
print("Compared Text....")

# Get message text and verify
user_message_text = driver.find_element(By.XPATH, "//span[@class='messageForUser']")
print("Comparison Text: " + str(user_message_text.text))

try:
    assert user_message_text.text == "The two texts are identical!"
    print("The Copy-and-Paste operation is verified!")
except AssertionError as err:
    print("The Copy-and-Paste does not match, Web UI has a bug with Selenium.'")

helper_functions.print_seperator(50)
time.sleep(2)

driver.close()
driver.quit()
