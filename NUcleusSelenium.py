from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import unittest
import datetime
import time
import random


def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)


class DailyDiary(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="path/to/driver")
        self.driver.get("https://nucleus.niituniversity.in")
        self.driver.maximize_window()

    def test_Login(self):
        driver = self.driver
        NUUserName = "ID"
        NUPass = "PASSWORD"
        date = datetime.datetime.now().day + datetime.datetime.now().month + datetime.datetime.now().year
        timeInHour = '09'
        timeInMin = '00'
        timeOutHour = '18'
        timeOutMin = '30'
        # description = 'Today we solved the S2 level bug. Also worked on the allotted views and have finished with the unit test of the view.'
        description = random_line('descriptions.txt')

        UserNameFieldId = 'SchSel_txtUserName'
        passwordFieldId = 'SchSel_txtPassword'
        LoginButtonId = 'SchSel_btnLogin'
        DailyDiaryButtonId = 'ctl00_ContentPlaceHolder1_btnDDiary'
        DatePickerId = 'wdcDate_input'
        TimeInHourId = 'Timeinhr'
        TimeInMinId =  'Timeinmin'
        TimeOutHourId = 'Timeouthr'
        TimeOutMinId = 'Timeoutmin'
        DescriptionId = 'txtDesc'
        DDSubmitButtonId = 'ctl00_ContentPlaceHolder1_btnSubmit'

        waitTimeMax = 30
        waitTimeMin = 10

        UserNameIdElement = WebDriverWait(driver, waitTimeMax).until(lambda driver: driver.find_element_by_id(UserNameFieldId))
        UserNameIdElement.clear()
        UserNameIdElement.send_keys(NUUserName)

        passwordElement = WebDriverWait(driver, waitTimeMax).until(lambda driver: driver.find_element_by_id(passwordFieldId))
        passwordElement.clear()
        passwordElement.send_keys(NUPass)

        loginButtonElement = WebDriverWait(driver, waitTimeMin).until(lambda driver: driver.find_element_by_id(LoginButtonId))
        loginButtonElement.click()

        DailyDiaryButtonElement = WebDriverWait(driver, waitTimeMin).until(lambda driver: driver.find_element_by_id(DailyDiaryButtonId))
        DailyDiaryButtonElement.click()

        datePickerElement = WebDriverWait(driver, waitTimeMin).until(lambda driver: driver.find_element_by_id(DatePickerId))
        datePickerElement.click()
        # datePickerElement.clear()
        datePickerElement.send_keys(date)
        datePickerElement.send_keys(Keys.TAB)

        timeInHourElement = WebDriverWait(driver, waitTimeMin).until(lambda driver: driver.find_element_by_id(TimeInHourId))
        timeInHourElement.click()
        timeInHourElement.send_keys(timeInHour)
        timeInHourElement.send_keys(Keys.TAB)

        timeInMinElement = WebDriverWait(driver, waitTimeMin).until(lambda driver: driver.find_element_by_id(TimeInMinId))
        timeInMinElement.click()
        timeInMinElement.send_keys(timeInMin)
        timeInMinElement.send_keys(Keys.TAB)

        timeOutHourElement = WebDriverWait(driver, waitTimeMin).until(lambda driver: driver.find_element_by_id(TimeOutHourId))
        timeOutHourElement.click()
        timeOutHourElement.send_keys(timeOutHour)
        timeOutHourElement.send_keys(Keys.TAB)

        timeOutMinElement = WebDriverWait(driver, waitTimeMin).until(lambda driver: driver.find_element_by_id(TimeOutMinId))
        timeOutMinElement.click()
        timeOutMinElement.send_keys(timeOutMin)
        timeOutMinElement.send_keys(Keys.TAB)

        descriptionElement = WebDriverWait(driver, waitTimeMin).until(lambda driver: driver.find_element_by_id(DescriptionId))
        descriptionElement.send_keys(description)

        DDSubmitButtonElement = WebDriverWait(driver, waitTimeMin).until(lambda driver: driver.find_element_by_id(DDSubmitButtonId))
        DDSubmitButtonElement.click()

        time.sleep(10)

