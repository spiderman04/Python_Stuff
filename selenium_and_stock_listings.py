
import datetime
import os
import pandas
import selenium.common.exceptions

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains

STOCK_INPUT_FILENAME = "nasdaq_top100.csv"
# STOCK_INPUT_FILENAME = "nyse_symbols_debug1.csv"  # list of 650 stocks
# STOCK_INPUT_FILENAME = "nyse_symbols_debug2.csv"
# STOCK_INPUT_FILENAME = "nyse_symbols_debug3.csv"
# STOCK_INPUT_FILENAME = "nasdaq_symbols_debug1.csv"  # list of 440 stocks
# STOCK_INPUT_FILENAME = "nasdaq_symbols_debug2.csv"
# STOCK_INPUT_FILENAME = "nasdaq_symbols_debug3.csv"
# STOCK_INPUT_FILENAME = "nasdaq_symbols_debug4.csv"

STOCK_SYMBOLS_NOT_ON_EXCHANGE_FILENAME = "symbols_not_on_exchange.txt"

FILE_MOVER_FREQ_MAX = 10
BANNER_OUTPUT = 40
TAKE_SCREENSHOTS = False


def get_current_date():
    """
    Returns a string based on the current date in the
    format of: <month>_<day>_<year>.

    :return: Return current date as string '<month>_<day>_year'

    reference: https://strftime.org/
    """

    dt = datetime.datetime.now()
    month = dt.strftime("%m")
    day = dt.strftime("%d")
    year = dt.strftime("%Y")
    # hours %I, minutes %M, seconds %S

    # return a string as '<month>_<day>_<year>'
    return str(month) + "_" + str(day) + "_" + str(year)


def get_current_time():
    dt = datetime.datetime.now()

    format1 = dt.strftime("%X %p")  # locale time hh:mm:ss AM/PM
    return format1


def get_log_string_name(the_date):
    """
    Build a string as a .csv file name based on the current date.
    Also, if there are multiple data files 1,2,3, the file name can
    be labeled differently on disk.

    :param the_date: Current date string
    :return:  a string of .csv file to write to
    """
    # which data file for adding log file extension name
    if STOCK_INPUT_FILENAME.__contains__("debug1"):
        extension = "_1.csv"
    elif STOCK_INPUT_FILENAME.__contains__("debug2"):
        extension = "_2.csv"
    elif STOCK_INPUT_FILENAME.__contains__("debug3"):
        extension = "_3.csv"
    elif STOCK_INPUT_FILENAME.__contains__("debug4"):
        extension = "_4.csv"
    else:
        extension = ".csv"

    # which file to append to
    if STOCK_INPUT_FILENAME.__contains__("nasdaq"):
        log_string = "log_nasdaq_" + the_date + extension
    elif STOCK_INPUT_FILENAME.__contains__("nyse"):
        log_string = "log_nyse_" + the_date + extension
    else:
        log_string = "log_" + the_date + extension

    return log_string


def free_stock_screener_site():
    # driver.get('https://stockanalysis.com/stocks/screener/')
    driver.maximize_window()

    # time.sleep(5)

    # assert driver.title == 'Free Stock Screener - Search, Filter and Analyze Stocks - Stock Analysis'

    # get page info for Symbol, Company Name, Market Cap, Price, % Change, Industry, Volume and PE Ratio
    # table_data =  driver.find_element(By.ID, "main-table")
    # print("Table Object: " + str(table_data))
    # print("Table Object Text: " + str(table_data.get_property("text")))
    # print("Table Data: " + str(table_data.get_property("text")))
    #
    # page_info = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/main/div[3]/nav/div/span/span')
    # page_info.location_once_scrolled_into_view()
    #
    # actions = ActionChains(driver)
    # actions.move_to_element(page_info).perform()
    # print(str(page_info.text()))

    # next button
    # driver.find_element(By.CLASS_NAME, 'hidden sm:inline').get_attribute('data-svelte-h').click()
    # time.sleep(10)


def log_problematioc_symbol(error_symbol):

    print("=" * BANNER_OUTPUT)
    print("There is an issue with symbol " + error_symbol)
    print("=" * BANNER_OUTPUT)

    # write all questionable symbols to a file at once versus within the loop above
    file2 = open(STOCK_SYMBOLS_NOT_ON_EXCHANGE_FILENAME, 'a')
    file2.write(error_symbol + '\n')
    file2.close()


def move_files(var_loop_counter, end_flag):

    date_string2 = get_current_date()
    archive_folder_name = date_string2.replace('_', '-') + "_archive"

    if (var_loop_counter % FILE_MOVER_FREQ_MAX) == 0:
        # only make folder once
        if var_loop_counter == FILE_MOVER_FREQ_MAX:
            print("Making archive folder once.")
            os.system(f"mkdir " + archive_folder_name)
        print("Moving " + str(FILE_MOVER_FREQ_MAX) + " screenshot files to archive folder...")
        os.system(f"move e:\\pycharmprojects\\examples\\*.png " + archive_folder_name)
    elif str(end_flag).upper() == 'TRUE':
        print("Moving remaining screenshots files to archive folder...")
        os.system(f"move e:\\pycharmprojects\\examples\\*.png " + archive_folder_name)


def get_nasdaq_stock(dvr, sym, lc):
    # https://www.nasdaq.com/market-activity/stocks/<symbol>

    try:
        base_url = "https://www.nasdaq.com/market-activity/stocks/"
        url = base_url + sym
        print("(" + str(lc) + ") Loading..." + url)

        dvr.get(url)
        dvr.get_full_page_screenshot_as_file(sym + "_nasdaq.png")

    except selenium.common.exceptions.WebDriverException:
        # bad url?
        dvr.get_full_page_screenshot_as_file(sym + "_nasdaq_error.png")
        pass


def get_barchart_stocks(dvr, sym, lc):
    # https://www.barchart.com/stocks/quotes/<symbol>
    try:
        base_url = "https://www.barchart.com/stocks/quotes/"
        url = base_url + sym
        print("(" + str(lc) + ") Loading..." + url)

        dvr.get(url)
        dvr.get_full_page_screenshot_as_file(sym + "_barchart.png")

    except selenium.common.exceptions.TimeoutException:
        dvr.get_full_page_screenshot_as_file(sym + "_googlefinance_timeout.png")
        pass


def get_google_finance(dvr, sym, lc):
    # https://www.google.com/finance/quote/<symbol>:<exchange> Exchange=NASDAQ or NYSE
    # Exchanges listed here: https://www.google.com/intl/en_US/googlefinance/disclaimer/

    url = ''
    base_url = "https://www.google.com/finance/quote/"
    if STOCK_INPUT_FILENAME.__contains__("nasdaq"):
        url = base_url + sym + ":NASDAQ"
    elif STOCK_INPUT_FILENAME.__contains__("nyse"):
        url = base_url + sym + ":NYSE"

    # customized check regardless of file name
    if sym.__contains__("INDEX"):
        # no need to add the exchange string to the URL
        url = base_url + sym

    # load the URL
    print("(" + str(lc) + ") Loading..." + url)
    driver.get(url)

    if TAKE_SCREENSHOTS is True:
        dvr.get_full_page_screenshot_as_file(sym + "_googlefinance.png")
    else:
        print("Ignoring browser screenshots.")

    # chcck for any page errors
    check_google_page_error(dvr, sym)

    get_price_and_log_data(dvr, sym, ".fxKbKc")


def check_google_page_error(dvr, sym):

    try:
        page_info = dvr.find_element(By.CLASS_NAME, "b4EnYd")

        if (page_info.text == "We could not find any match for your search." or
                page_info.text == "We couldn't find any match for your search."):

            log_problematioc_symbol(sym)

    except selenium.common.exceptions.NoSuchElementException:
        # Error page not found!
        pass


def get_stock_analysis(dvr, sym, lc):
    # https://stockanalysis.com/stocks/<symbol>/

    base_url = "https://stockanalysis.com/stocks/"
    url = base_url + sym
    print("(" + str(lc) + ") Loading..." + url)
    dvr.get(url)
    dvr.get_full_page_screenshot_as_file(sym + "_stockanalysis.png")
    check_stock_analysis_page_error(dvr, sym)


def check_stock_analysis_page_error(dvr, sym):

    try:
        page_info = dvr.find_element(By.CLASS_NAME, "b4EnYd")

        if (page_info.text == "Page Not Found - 404" or
                page_info.text == "Page Not Found - 404"):

            log_problematioc_symbol(sym)

    except selenium.common.exceptions.NoSuchElementException:
        # Error page not found!
        pass


def get_price_and_log_data(dvr, sym, obj):

    try:
        page_info = dvr.find_element(By.CSS_SELECTOR, obj)
        print("Current Price: " + page_info.text + " at " + get_current_time())

        # get current date as custom string for log file (nasdaq vs. nyse)
        date_string2 = get_current_date()
        log_string = get_log_string_name(date_string2)

        # log new data
        file2 = open(log_string, 'a+')
        price_without_comma = page_info.text.replace('$', '').replace(',', '')
        current_time = get_current_time()

        file2.write(date_string2.replace('_', '/') + "," +
                   current_time + "," +
                   sym + "," +
                   str(price_without_comma) + '\n')
        file2.close()

    except selenium.common.exceptions.NoSuchElementException:
        # Error page not found!
        pass


if __name__ == '__main__':

    # placeholder for start of program, used to get duration of time at the end
    program_start = datetime.datetime.now()

    # input_files = []
    # objs = os.scandir()
    # for obj in objs:
    #     if obj.is_file() and obj.name.__contains__(".csv"):
    #         input_files.append(obj.name)

    options = webdriver.FirefoxOptions()            # options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    # driver.maximize_window()
    driver.implicitly_wait(5)

    # setup data frame with preset headers
    print("Reading input file '" + STOCK_INPUT_FILENAME + "' for symbols...")
    df = pandas.read_csv(STOCK_INPUT_FILENAME, header=0, names=['Id', 'Symbol', 'Name'])
    symbols = df['Symbol']
    # not used at this time
    # companies = df['Name']

    # create simple log file for reporting error symbols
    with open(STOCK_SYMBOLS_NOT_ON_EXCHANGE_FILENAME, 'w') as file:
        file.write("Symbols not on NASDAQ, an error with Google Finance Webpage, or delisted.\n")
    file.close()

    loop_counter = 0
    for symbol in symbols:
        # debug
        # if loop_counter == 4:
        #    break
        loop_counter = loop_counter + 1

        # check the data type from the input, in one case symbol 'NAN' was considered a float as Python not-a-number
        if symbol is not float:

            get_google_finance(driver, symbol, loop_counter)
            # stock_analysis(driver, symbol, loop_counter)
            # nasdaq(driver, symbol, loop_counter)
            # barchart_stocks(driver, symbol, loop_counter)

            # check each output file of say, 30 (constant) and move to an archive folder
            if TAKE_SCREENSHOTS is True:
                move_files(loop_counter, "false")
            else:
                continue
        else:
            print("=" * BANNER_OUTPUT)
            print("A bizarre FLOAT type was found at row " + str(loop_counter) + " !!")
            print("Script will continue...")
            print("=" * BANNER_OUTPUT)

    # close all webdriver handles and release memory
    driver.stop_client()
    driver.close()
    driver.quit()

    # move overflow screenshots files
    if TAKE_SCREENSHOTS is True:
        move_files(-99, 'true')

    # get script ending time and calculate duration of script execution
    program_end = datetime.datetime.now()
    duration = (program_end - program_start)

    # echo script duration metrics
    print("=" * BANNER_OUTPUT)
    rounded = round(duration.total_seconds(), 3)
    print("Script duration in seconds: " + str(rounded))
    rounded = round(duration.total_seconds() / 60.00, 3)
    print("Script duration in minutes: " + str(rounded))
    rounded = round(duration.total_seconds() / 3600.00 , 3)
    print("Script duration in hours:   " + str(rounded))
    print("=" * BANNER_OUTPUT)

    # move log file to separate folder 'logs' for archival
    print("Moving log file....")
    file_path = os.getcwd()

    date_string = get_current_date()
    log_string_name = get_log_string_name(date_string)

    log_filename = os.path.join(file_path, log_string_name)
    print("Moving file " + log_filename + " to 'logs' folder...")

    os.popen("move " + log_filename + " logs")
