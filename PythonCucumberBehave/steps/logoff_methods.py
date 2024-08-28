from behave import Given, When, Then
from selenium import webdriver
from selenium.webdriver.common.by import By

@Given('Verify Home Page')
def verify_home_page(context):
    print("Verify Home page")
    assert "Login: Mercury Tours" == context.driver.title


@When('Verify Home Page')
def verify_home_page(context):
    print("Verify Home page")
    assert "Login: Mercury Tours" == context.driver.title


@Then ('Logoff and close browser2')
def logoff_and_close_browser2(context):
    print("Logoff and close browser")
    context.driver.find_element(By.LINK_TEXT, "SIGN-OFF").click()
    context.driver.close()
    context.driver.quit()

