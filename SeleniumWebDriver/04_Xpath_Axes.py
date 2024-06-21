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

driver.get(constants.URL_MONEY_GAINERS)

# XPATH AXES TYPES WE CAN USE
# self (current node), parent, child, ancestor, descendant, following, following-sibling, preceding,
# preceding-sibling, attribute, namespace, descendant-or-self, ancestor-or-self

# self
self_node = driver.find_element(By.XPATH, "//a[contains(text(), 'India Tourism De')]/self::a").text
print("Self Node: " + self_node)
assert self_node == "India Tourism De"

# parent
parent_node = driver.find_element(By.XPATH, "//a[contains(text(), 'India Tourism De')]/parent::td").text
print("Parent Node of Self: " + parent_node)
assert self_node == "India Tourism De"

# child
child_nodes = driver.find_elements(By.XPATH, "//a[contains(text(), 'India Tourism De')]/ancestor::tr/child::td")
for child in child_nodes:
    print("Child Node of Self: " + str(child.text))
    #    print("Child Node of Self: " + driver.find_element(By.XPATH, child_node).text())

# ancestor
ancestor_node = driver.find_element(By.XPATH, "//a[contains(text(), 'India Tourism De')]/ancestor::tr").text
print("Ancestor Node of Self: " + ancestor_node)
assert ancestor_node.__contains__("India Tourism De")

# descendent
descendant_nodes = driver.find_elements(By.XPATH, "//a[contains(text(), 'India Tourism De')]/ancestor::tr/descendant::*")
print("Number of Descendant Nodes of Self: " + str(len(descendant_nodes)))
assert len(descendant_nodes) == 7, "Descendant nodes don't match 7"

# following
following_nodes = driver.find_elements(By.XPATH, "//a[contains(text(), 'India Tourism De')]/ancestor::tr/following::*")
print("Number of Following Nodes of Self: " + str(len(following_nodes)))
assert len(following_nodes) > 0, "There are no following nodes of Self."

# following-sibling
following_nodes = driver.find_elements(By.XPATH, "//a[contains(text(), 'India Tourism De')]/ancestor::tr/following-sibling::tr")
print("Number of Following-Sibling Nodes of Self: " + str(len(following_nodes)))

# preceding
preceding_nodes = driver.find_elements(By.XPATH, "//a[contains(text(), 'India Tourism De')]/ancestor::tr/preceding::tr")
print("Number of Preceding Nodes of Self: " + str(len(following_nodes)))

# preceding-sibling
preceding_nodes = driver.find_elements(By.XPATH, "//a[contains(text(), 'India Tourism De')]/ancestor::tr/preceding-sibling::tr")
print("Number of Preceding-Sibling Nodes of Self: " + str(len(following_nodes)))

driver.close()
driver.quit()
