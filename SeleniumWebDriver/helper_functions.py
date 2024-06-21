import os

from selenium import webdriver
from selenium.webdriver.common.by import By


def count_links(driver):
    hyperlinks = driver.find_elements(By.TAG_NAME, "a")
    print(str(len(hyperlinks)) + " Links on page: " + driver.current_url)
    print("\r\n")


def print_seperator(iterator=25):
    output = ""
    for i in range(1, iterator+1):
        output = output + "="
    print(output)


def setup_chrome():

    from selenium.webdriver.chrome.service import Service
    # Override the Chrome Options
    custom_options = webdriver.ChromeOptions()
    custom_options.add_argument("--disable-notifications")
    custom_options.add_argument("--start-fullscreen")
    custom_options.add_argument("--disable-popup-blocking")
    custom_options.add_argument("--disable-plugins")
    custom_options.add_argument('--no-sandbox')
    #custom_options.add_argument('--headless')
    custom_options.add_argument('--disable-setuid-sandbox')
    custom_options.add_argument('--disable-dev-shm-usage')
    custom_options.add_argument('--disable-gpu')

    # Download the file to Project folder
    print("Working Folder for Chrome: " + str(os.getcwd()))
    custom_preferences = {"download.default_directory": os.getcwd()
        , "plugins.always_open_pdf_externally": True}

    custom_options.add_experimental_option("prefs", custom_preferences)

    service_object = Service("C:\\WebDrivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_object, options=custom_options)
    driver.implicitly_wait(20)
    driver.maximize_window()

    return driver


def setup_edge():

    from selenium.webdriver.edge.service import Service

    # Override the Edge Options
    custom_options = webdriver.EdgeOptions()
    custom_options.add_argument("--disable-notifications")
    custom_options.add_argument("--start-fullscreen")
    custom_options.add_argument("--disable-popup-blocking")
    custom_options.add_argument("--disable-plugins")

    # Download the file to Project folder
    print("Working Folder: " + str(os.getcwd()))
    custom_preferences = {"download.default_directory": os.getcwd()}

    custom_options.add_experimental_option("prefs", custom_preferences)

    service_object = Service("C:\\WebDrivers\\msedgedriver.exe")
    driver = webdriver.Edge(service=service_object, options=custom_options)
    driver.implicitly_wait(20)
    driver.maximize_window()

    return driver


def setup_firefox():

    from selenium.webdriver.firefox.service import Service
    from selenium.webdriver import FirefoxProfile
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

    # Ensure we don't attempt to use the new geckodriver method (which
    # isn't working for us. I _think_ selenium 2 defaults to old method,
    # but just to make sure.
    # capabilities = DesiredCapabilities.FIREFOX
    # capabilities['marionette'] = False

    print("Working Folder for Firefox: " + str(os.getcwd()))
    custom_options = webdriver.FirefoxOptions()
    custom_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/msword")
    custom_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    custom_options.set_preference("browser.download.manager.showWhenStaring", False)
    custom_options.set_preference("browser.download.folderList", 2)  # 0=Desktop, 1=Default location, 2=Custom
    custom_options.set_preference("browser.download.dir", os.getcwd())
    custom_options.set_preference("pdfjs.disabled", True)

    service_object = Service("C:\\WebDrivers\\geckodriver.exe")
    driver = webdriver.Firefox(service=service_object, options=custom_options)

    driver.implicitly_wait(20)
    driver.maximize_window()

    return driver
