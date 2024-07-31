import time

import pytest
import softest
from selenium.webdriver.common.by import By
from pages.yatraLaunchPage import LaunchPage
from utilities.utils import Utils
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("setup")
@ddt
class Testsearchflight(softest.TestCase):
    log = Utils.custom_logger()

    @pytest.fixture(autouse=True)
    def class_setup_object_creation(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()

    #@data(*Utils.read_data_from_exel("C:\\PythonSelenium\\TestFrameworkDemo\\testdata\\InputData.xlsx", "Sheet1"))
    @data(*Utils.read_data_from_csv("C:\\PythonSelenium\\TestFrameworkDemo\\testdata\\InputTestData.csv"))
    @unpack
    def test_demosearchflight_1stop(self, goingfrom, goingto, depdate, stopsnumber):
        # Launching the browser and opening the travel website
        # Provide going from location, going to location, Selecting departure date & Click on the Search Flights
        sp = self.lp.demo_searchFlights(goingfrom, goingto, depdate)
        # Dynamic Scroll
        self.lp.page_scroll()
        #Selecting "1 Stop" Filter
        sp.selectingStop(stopsnumber)
        allstops1 = sp.wait_for_presence_of_all_elements_located(By.XPATH, "//span[contains(text(), 'Non Stop') or contains(text(), '1 Stop') or contains(text(), '2 Stop')]")
        self.log.info(len(allstops1))
        # Verify that the filtered results shows flights having only 1 stop
        self.ut.asserting_elements(allstops1, stopsnumber)

    time.sleep(3)