# TO FILL:
"""
LINE 27: THE DRIVER PATH (CHROME)
LINE 51: THE USERNAME
LINE 52: THE PASSWORD
LINE 97: THE START MONTH
LINE 98: THE STOP MONTH
"""

##############
#  LIBRARY   #
##############

from selenium import webdriver
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def open_site():
    """
    function that opens the site on full screen and return the driver opened
    :return: the driver
    """
    PATH = 'TO FILL: THE DRIVER PATH'        # the driver path
    WEB = 'TO FILL: THE URL OF THE SITE'       # the site address
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)     # keep the window open
    browser = webdriver.Chrome(options=options, executable_path=PATH)
    browser.get(WEB)
    time.sleep(2)                   # loading time
    browser.maximize_window()        # full screen
    return browser

def first_log(browser):
    """ function that get into the login in the first time """
    # login into account
    elem = browser.find_element_by_class_name('homeContinueBg')
    elem.click()
    time.sleep(2)                   # loading time

def login(browser):
    """
    function that login into site
    :param browser: the driver opened
    :return: none
    """
    # LOGIN DETAILS
    USERNAME = "TO FILL: THE MAIL OF THE USER"
    PASSWORD = "TO FILL: THE PASSWORD"

    # puts email
    email_bar = browser.find_element_by_id('user_email')
    email_bar.send_keys(USERNAME)
    # puts password
    password_bar = browser.find_element_by_id('user_password')
    password_bar.send_keys(PASSWORD)
    # click checkbox
    policy_bar = browser.find_element_by_id('policy_confirmed')
    browser.execute_script("arguments[0].click();", policy_bar)
    # click on login
    log_in = browser.find_element_by_name("commit")
    log_in.click()
    time.sleep(2)  # loading time

def set_new_meeting(browser):
    """
    function that set new meeting
    :param browser: the driver opened
    :return: none
    """
    # click on continue
    elem = browser.find_element_by_link_text('המשך')
    elem.click()
    time.sleep(2)  # loading time
    # click on new meeting
    elem = browser.find_element_by_link_text('קבע פגישה מחדש')
    elem.click()
    time.sleep(1)  # loading time
    # click on continue
    elem = browser.find_element_by_css_selector('a.accordion-title')
    action = webdriver.common.action_chains.ActionChains(browser)
    action.move_to_element_with_offset(elem, 900, 280)     # move the offset
    action.click()
    action.perform()
    time.sleep(2)  # loading time

def set_date(browser):
    """
    function that check for available dates in celendar and refresh until he get one
    :param browser: the driver opened
    :return: the date that i choose
    """
    # INITIALIZE
    skip_month = 5         # TO CHANGE (THE MONTH YOU START FROM) (0 MEANS THE CURRENT MONTH)
    BORDER = 9             # TO CHANGE (THE MONTH ITS ENDS CHECKING ON AND RESET) (NEEDS TO BE MORE THAN THE skip_month)
    refresh_count = 0

    # get the start time
    now = datetime.now()
    start_time = now.strftime("%H:%M:%S")

    try:
        while 0 == 0:       # its take 4 hours before relogin...
            skip_month = 5
            # open the Celendar
            elem = browser.find_element_by_id("appointments_consulate_appointment_date_input")
            elem.click()
            time.sleep(1)  # loading time
            # skip months
            for i in range(skip_month):
                # next page
                elem = browser.find_element_by_link_text("Next")
                elem.click()
                # print("NEXT PAGE..")
                time.sleep(0.25)  # loading time
            while skip_month < BORDER:
                for j in range(1, 6):
                    for k in range(1, 7):
                        # print("row: " + str(j) + " col: " + str(k))
                        # click on every day
                        elem = browser.find_element_by_xpath("/html/body/div[5]"
                                                             "/div[2]/table/tbody/tr[" + str(j) +"]/td[" + str(k) + "]")
                        elem.click()
                        time.sleep(0.25)  # loading time
                # next page
                skip_month += 1
                elem = browser.find_element_by_link_text("Next")
                elem.click()
            # refresh page
            browser.refresh()
            refresh_count += 1
            time.sleep(3)  # loading time
            # prints the times and the amount of refreshes
            print("refresh count: " + str(refresh_count))
            print("Start Time =", start_time)
            # get the current time
            now = datetime.now()
            end_time = now.strftime("%H:%M:%S")
            print("End Time =", end_time)
            # gets the total amount of the time the program is working
            copy_start_time = start_time.replace(':', '')
            copy_start_time_min = int(copy_start_time[2:4])
            copy_start_time = int(copy_start_time[:2])
            copy_end_time = end_time.replace(':', '')
            end_time_min = int(copy_end_time[2:4])
            copy_end_time = int(copy_end_time[:2])
            total_time = (copy_end_time - copy_start_time)
            if end_time_min < copy_start_time_min:          # for example 8:40 to 9:30 is less than a hour
                total_time -= 1
            if total_time < 0:      # extreme case
                total_time = 0
            print("Total Time =", str(total_time) + " Hours")
            print("---------------------")

    except:     # check if you find date
        if total_time != 4:   # less than 4 the amount of hours before reconnect
            print("Done!")
            # prints the times and the amount of refreshes
            print("refresh count: " + str(refresh_count))
            print("Start Time =", start_time)
            now = datetime.now()        # get the current time
            end_time = now.strftime("%H:%M:%S")
            print("End Time =", end_time)
            date = "row: " + str(j) + " col: " + str(k) + " month: " + str(skip_month - 4)
            print(date)
            # set time
            elem = browser.find_element_by_xpath('/html/body/div[4]/main'
                                                 '/div[4]/div/div/form/fieldset/ol/fieldset/div/div[2]/div[3]/li[2]/select')
            elem.click()
            time.sleep(1)  # loading time
            elem = browser.find_element_by_xpath('/html/body/div[4]/main'
                                                 '/div[4]/div/div/form/fieldset'
                                                 '/ol/fieldset/div/div[2]/div[3]/li[2]/select/option[2]')
            elem.click()
            time.sleep(1)  # loading time

            print("SENDS...")
            # click on finish
            elem = browser.find_element_by_xpath('/html/body/div[4]'
                                                 '/main/div[4]/div/div/form/div[2]/fieldset/ol/li/input')
            elem.click()
            time.sleep(1)  # loading time
            elem = browser.find_element_by_xpath('/html/body/div[6]/div/div/a[2]')
            elem.click()
            time.sleep(1)  # loading time
            print("SENT!")
            time.sleep(1)  # loading time
        else:
            print("ReLogin...")
            time.sleep(2)  # loading time
            # click on ok soo the site will not think that you are afk
            elem = browser.find_element_by_xpath('/html/body/div[6]/div[3]/div/button')
            elem.click()
            time.sleep(2)  # loading time
            start_time = end_time
            start_prog(browser)

    return date

def start_prog(browser):
    """ like second main that used for reconnecting without closing the site and open new one """
    date = ""
    login(browser)
    set_new_meeting(browser)
    date = set_date(browser)

def main():
    try:
        browser = open_site()   # opens the site
        first_log(browser)      # get into the login
        start_prog(browser)     # infinity loop of getting date
    except:
        print("Exit!")


if __name__ == "__main__":
    main()

