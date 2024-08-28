
from behave import Given, When, Then
from selenium import webdriver
from selenium.webdriver.common.by import By


@Given('Open Browser')
def open_browser(context):
    print("Open Browser")
    context.driver = webdriver.Firefox()
    context.driver.get("https://demo.guru99.com/test/newtours/")


@When('Providing valid "{username}" and "{password}"')
def provide_username_and_password(context, username, password):
    print("Provide username and password")
    context.driver.find_element(By.NAME, "userName").send_keys(username)
    context.driver.find_element(By.NAME, "password").send_keys(password)
    context.driver.find_element(By.NAME, "submit").click()


@Then('Verify Home Page')
def verify_home_page(context):
    print("Verify Home page")

    # will only pass for a seccussful login!
    assert "Login: Mercury Tours" == context.driver.title

@Then('Verify Success Message')
def verify_success_message(context):
    try:
        text = context.driver.find_elemnt(By.XPATH, "//h3[text()='Login Successfully']").text
        if text == "Login Successfully":
            assert True, "Testcase passed."
    except:
        assert False, "Testcase failed"


@Then ('Logoff and close browser')
def logoff_and_close_browser(context):
    print("Logoff and close browser")
    context.driver.find_element(By.LINK_TEXT, "SIGN-OFF").click()
    context.driver.close()
    context.driver.quit()

@When('Verify login by using below query')
def verify_login_as_table(context):

    for row in context.table:
        context.driver.find_element(By.NAME, "userName").send_keys(row["username"])
        context.driver.find_element(By.NAME, "password").send_keys(row["password"])
        context.driver.find_element(By.NAME, "submit").click()
