import time
import logging


from selenium.webdriver.common.by import By
from base.base_driver import basedriver
from utilities.utils import Utils


class searchPage(basedriver):
    log = Utils.custom_logger()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    FILTER_BY_1_STOP = "//p[normalize-space()='1']"
    FILTER_BY_2_STOP = "//p[normalize-space()='2']"
    FILTER_BY_NON_STOP = "//p[normalize-space()='0']"

    def get_filter_by_one_stop(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_1_STOP)

    def get_filter_by_two_stop(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_2_STOP)

    def get_filter_by_no_stop(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_NON_STOP)

    def selectingStop(self, by_stop):
        if by_stop == "1 Stop":
            self.get_filter_by_one_stop().click()
            self.log.debug("Selected Flights with one stop")
            time.sleep(2)
        elif by_stop == "2 Stop":
            self.get_filter_by_two_stop().click()
            self.log.info("Selected Flights with two stop")
            time.sleep(2)
        elif by_stop == "Non Stop":
            self.get_filter_by_no_stop().click()
            self.log.warning("Selected Flights with no stop")
            time.sleep(2)
        else:
            self.log.warning("Please provide valid input: ")


        # self.driver.find_element(By.XPATH, "//p[normalize-space()='1']").click()
        # time.sleep(2)