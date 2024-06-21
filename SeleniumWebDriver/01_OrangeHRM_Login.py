import constants
from selenium import webdriver
from selenium.webdriver.common.by import By

# Python will look in SCRIPTS path OR specify absolute path
driver = webdriver.Chrome(executable_path="C:\\WebDrivers\\chromedriver.exe", service_args=None)
driver.get(constants.URL_ORANGEHRM)
assert driver.title == 'OrangeHRM'

driver.find_element(By.ID, "txtUsername").clear()
driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, 'txtPassword').send_keys('admin123')
driver.find_element(By.ID, 'btnLogin').click()

try:
    assert driver.title == 'OrangeHRM2'
    print("The page title is verified!")
except AssertionError as err:
    print("The page TITLE does not match 'OrangeHRM'")

driver.close()
driver.quit()
