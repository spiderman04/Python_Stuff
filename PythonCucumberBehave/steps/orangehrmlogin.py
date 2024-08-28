
from behave import Given, When, Then
from selenium import webdriver
from selenium.webdriver.common.by import By

@Given(u'I launch Firefox Browser')
def launch_firefox(context):
    context.driver = webdriver.Firefox()


@When(u'I open orange HRM homepage')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.driver.implicitly_wait(10)


@When(u'Enter username "{user}" and password "{pwd}"')
def enter_username_and_password(context, user, pwd):
    context.driver.find_element(By.NAME, "username").send_keys(user)
    context.driver.find_element(By.NAME, "password").send_keys(pwd)


@When(u'Click on login button')
def click_login(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
    # btnLogin

@Then(u'User must successfully login to the Dashboard page')
def verify_dashboard(context):
    try:
        text = context.driver.find_element(By.XPATH, "//h1[contains(text(), 'Dashboard')]").text
        assert text == 'Dashboard'
    except:
        assert False, "Test Failed"

    context.driver.close()

