import logging
import time
from selenium.webdriver.common.by import By
from base.base_driver import basedriver
from pages.search_flights_resultpage import searchPage



class LaunchPage(basedriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    DEPART_FROM_FIELD = "//input[@id = 'BE_flight_origin_city']"
    GOING_TO_FIELD = "//input[@id='BE_flight_arrival_city']"
    DEPART_FROM_GOING_TO_SEARCH_FIELD = "//div[@class='viewport']//div[1]//li"
    DEPARTURE_DATE_FIELD = "//input[@id='BE_flight_origin_date']"
    DEPARTURE_DATE_SUGGESTION_FIELD = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD weekend' and @class!='inActiveTD']"
    SEARCH_BUTTON = "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']"

    def getDepartfrom(self):
        return self.wait_for_until_element_is_clickable(By.XPATH, self.DEPART_FROM_FIELD)

    def getGoingto(self):
        return self.wait_for_until_element_is_clickable(By.XPATH, self.GOING_TO_FIELD)

    def getDepartfromGoingtoSearch(self):
        # return self.wait_for_until_element_is_clickable(By.XPATH, self.DEPART_FROM_GOING_TO_SEARCH_FIELD)
        return self.driver.find_elements(By.XPATH, self.DEPART_FROM_GOING_TO_SEARCH_FIELD)

    def getDepartdate(self):
        return self.wait_for_until_element_is_clickable(By.XPATH, self.DEPARTURE_DATE_FIELD)

    def getDepartdatelist(self):
        return self.driver.find_elements(By.XPATH, self.DEPARTURE_DATE_SUGGESTION_FIELD)

    def getSearch(self):
        return self.wait_for_until_element_is_clickable(By.XPATH, self.SEARCH_BUTTON)
    def departfrom(self, departlocation):
        self.getDepartfrom().click()
        time.sleep(2)
        self.getDepartfrom().send_keys(departlocation)
        time.sleep(2)
        goingfromSearch = self.getDepartfromGoingtoSearch()
        print(len(goingfromSearch))
        for goingfromResults in goingfromSearch:
            if "Mumbai" in goingfromResults.text:
                goingfromResults.click()
                time.sleep(2)
                break

    def going_to(self, goingtolocation):
        self.getGoingto().send_keys(goingtolocation)
        time.sleep(2)
        goingtoSearch = self.getDepartfromGoingtoSearch()
        print(len(goingtoSearch))
        for goingtoResults in goingtoSearch:
            if "New Delhi" in goingtoResults.text:
                goingtoResults.click()
                time.sleep(2)
                break

    def departdate(self, departuredate):
        self.getDepartdate().click()
        time.sleep(2)
        startDateSearch = self.getDepartdatelist()
        for startDateResults in startDateSearch:
            if startDateResults.get_attribute("data-date") == departuredate:
                startDateResults.click()
                time.sleep(2)
                break

    def clicksearch(self):
        self.getSearch().click()
        time.sleep(3)

    def demo_searchFlights(self, departlocation, goingtolocation, departuredate):
        self.departfrom(departlocation)
        self.going_to(goingtolocation)
        self.departdate(departuredate)
        self.clicksearch()
        sp = searchPage(self.driver)
        return sp
