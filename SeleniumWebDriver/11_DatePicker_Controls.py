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

print("Loading URL: " + constants.URL_DATEPICKER_STANDARD)
driver.get(constants.URL_DATEPICKER_STANDARD)
helper_functions.print_seperator(50)

# Standard Date Picker control from JQueryUI website, format is mm/dd/yyyy
driver.switch_to.frame(0)
driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("01/24/2022")
driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys('\r\n')

# Non-standard way of working with the Date Picker control
driver.get(constants.URL_DATEPICKER_STANDARD)
driver.switch_to.frame(0)
driver.find_element(By.XPATH, "//input[@id='datepicker']").click()

selection_month = "June"
selection_day = "20"
selection_year = "2023"

while True:

    gui_month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    gui_year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if gui_month == selection_month and gui_year == selection_year:
        break
    else:# Next button
       driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click()
    # else:  # Prev button
        # driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[1]/span").click()

    # selectDay
    days_in_calendar = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
    for days in days_in_calendar:
        if days.text == selection_day:
            days.click()
            break


time.sleep(1)

driver.close()
driver.quit()
