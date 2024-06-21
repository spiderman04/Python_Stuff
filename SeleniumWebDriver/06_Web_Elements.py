import os
import constants
import helper_functions
import requests   # From Settings/Project Intrepter/requests package

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

local_path = os.path.dirname(__file__)
print("Base Name: " + os.path.basename(__file__))
print("Directory Name: " + os.path.dirname(__file__))

# Python will look in SCRIPTS path OR specify absolute path
driver = webdriver.Chrome(executable_path="E:\\WebDrivers\\chromedriver.exe") #, service_args=None)
# driver.maximize_window()

driver.get(constants.URL_WEB_ELEMENTS_PRACTICE_FORM)

# Select all Checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")
print("Checkbox Web Elements Count: " + str(len(checkboxes)))

# Option #1: Check the box by Range() method
for i in range(len(checkboxes)):
    print("Checkbox Item: " + str(checkboxes[i].get_attribute('id')))
    checkboxes[i].click()
helper_functions.print_seperator()

# Option #2: Check the box using element
for checkbox in checkboxes:
    print("Checkbox Item: " + str(checkbox.get_attribute('id')))
    checkbox.click()
helper_functions.print_seperator()

# Conditional check by week name
for checkbox in checkboxes:
    print("Checkbox Item: " + str(checkbox.get_attribute('id')))
    weekname = checkbox.get_attribute('id')
    if weekname == 'monday' or weekname == 'sunday':
        checkbox.click()
helper_functions.print_seperator()

# Conditional for last 2 checkboxes but CLEAR first
for checkbox in checkboxes:
    print("Checkbox Item: " + str(checkbox.get_attribute('id')))
    if checkbox.is_selected():
        checkbox.click()

starting_index = len(checkboxes) - 2
print(str(starting_index))
for i in range(starting_index, len(checkboxes)):
    print("Checkbox Item: " + str(checkboxes[i].get_attribute('id')))
    checkboxes[i].click()
helper_functions.print_seperator()

# Conditional for first 2 checkboxes but CLEAR first
for checkbox in checkboxes:
    print("Checkbox Item: " + str(checkbox.get_attribute('id')))
    if checkbox.is_selected():
        checkbox.click()

starting_index = len(checkboxes) - 2
print(str(starting_index))
for i in range(len(checkboxes)):
    if i < 2:
        print("Checkbox Item: " + str(checkboxes[i].get_attribute('id')))
        checkboxes[i].click()
helper_functions.print_seperator()

# Hyperlink - Internal/External
driver.get(constants.URL_DEMO_NOPCOMMERCE)

driver.find_element(By.LINK_TEXT, "Digital downloads").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Digital").click()

# Hyperlink - Find all links
all_hyperlinks = driver.find_elements(By.TAG_NAME, "a")
all_hyperlinks2 = driver.find_elements(By.XPATH, "//a")
print("Web Page: " + constants.URL_DEMO_NOPCOMMERCE)
print("Hyperlink Count by Tag Name: " + str(len(all_hyperlinks)))
print("Hyperlink Count by XPATH: " + str(len(all_hyperlinks2)))

# Print all link names
for link in all_hyperlinks:
    if link.text != "":
        print("Hyperlink Text: " + link.text)
helper_functions.print_seperator()

# Hyperlink - Broken link
print(constants.URL_DEAD_LINK_CITY)
driver.get(constants.URL_DEAD_LINK_CITY)
all_hyperlinks = driver.find_elements(By.TAG_NAME, "a")

link_count = len(all_hyperlinks)
valid_link = 0
broken_link = 0
for link in all_hyperlinks:
    href_url = link.get_attribute('href')

    try:
        results = requests.head(href_url)
        if results.status_code >= 400:
            broken_link += 1
            print("Broken Link: " + href_url)
        else:
            valid_link += 1
            print("Valid Link: " + href_url)
    except Exception as exp:
        print("NO OP?" + str(exp))


print("Valid Link Count: " + str(valid_link))
print("Broken Link Count: " + str(broken_link))
helper_functions.print_seperator()

# Dropdowns
print(constants.URL_OPENCART)
driver.get(constants.URL_OPENCART)
all_country_options = driver.find_elements(By.XPATH, "//select[@id='input-country']")
print("Link Count: " + str(len(all_country_options)))

for option in all_country_options:
    print(option.text)
helper_functions.print_seperator()

# Select an Option or visible text
print(constants.URL_OPENCART)
driver.get(constants.URL_OPENCART)
country_name = Select(driver.find_element(By.XPATH, "//select[@id='input-country']"))
country_name.select_by_visible_text("Australia")
country_name.select_by_value("10")  # Value attribute is 'Argentina'
country_name.select_by_index(223)  # United States

# Print all options using the Options method
all_options = country_name.options
print("Total number of Options are: " + str(len(all_options)))

for option in all_options:
    if option.text == "United States":
        print("Selected Option Text: " + str(option.text))
        option.click()
        break

driver.close()
driver.quit()
