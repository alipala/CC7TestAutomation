import time
import unittest
import sys
import os
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from webui.Pages.cc7_loginPage import LoginPage
from webui.Tests.cc7_login import LoginTest
from webui.Pages.cc7_homePage import HomePage
from webui.Pages.cc7_stationconfigurationPage import StationConfigurationPage
from webui.Base.cc7_base import TestBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class StationConfigurationTest(TestBase):

    __server_ip_address = "https://192.168.3.55"
    __station_id_address = "192.168.3.90"
    __station_name = "cpu1500"

    def test_01_login(self):
        driver = self.driver
        self.df = pd.read_excel(os.getcwd() + self.__user_data_file)
        driver.get(self.__server_ip_address)
        login = LoginPage(driver)
        login.enter_username(self.df.iloc[0][0])  # username
        login.enter_password(self.df.iloc[0][1])  # password
        login.click_login()

    def test_02_station_configuration(self):
        driver = self.driver
        configuration = StationConfigurationPage(driver)
        configuration.nav_station_configuration_page()
        configuration.enter_station_name(self.__station_name)
        configuration.add_station()
        configuration.navigate_to_s7()
        configuration.enter_ip_address(self.__station_id_address)
        configuration.select_controller_family()
        configuration.click_save()
        time.sleep(5)
        configuration.apply_changes()
        print("Closure activities...")
        time.sleep(5)
        homepage = HomePage(driver)
        homepage.click_logout()


if __name__ == "__main__":
    unittest.main()
