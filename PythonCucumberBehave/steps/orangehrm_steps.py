
from behave import Given, When, Then
from selenium import webdriver
from selenium.webdriver.common.by import By


@Given(u'Launch Firefox Browser')
def launch_firefox(context):
    context.driver = webdriver.Firefox()


@When(u'open orange hrm homepage')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.driver.implicitly_wait(10)


@Then(u'verify logo present on page')
def verify_logo(context):
    try:
        status =  context.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[1]/img")
        assert status is True
    except:
        print("Testcase failed.")

@Then(u'close browser')
def close_browser(context):
    context.driver.close()
    context.driver.quit()

