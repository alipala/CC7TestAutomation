import unittest
import time
import sys
import os
import pandas as pd
sys.path.append((os.path.join(os.path.dirname(__file__), "..", "..")))
from webui.Pages.cc7_loginPage import LoginPage
from webui.Pages.cc7_homePage import HomePage
from webui.Pages.cc7_firmwareupdatePage import FirmwareUpdatePage
from webui.Base.cc7_base import TestBase

class FirmwareUpdateTest(TestBase):

    __server_ip_address = "https://192.168.3.55"
    __station_id_address = "192.168.3.90"
    __station_name = "cpu1500"
    __user_data_file = r"\login_details.xlsx"

    def test_01_login(self):
        driver = self.driver
        self.df = pd.read_excel(os.getcwd() + self.__user_data_file)
        driver.get(self.__server_ip_address)
        login = LoginPage(driver)
        login.enter_username(self.df.iloc[0][0])  # username
        login.enter_password(self.df.iloc[0][1])  # password
        login.click_login()

    def test_02_firmware_file_operation(self):
        driver = self.driver
        firmware = FirmwareUpdatePage(driver)
        firmware.nav_maintenance_page()
        firmware.browse_firmware_file()
        time.sleep(10)

    def test_03_click_to_update(self):
        driver = self.driver
        update = FirmwareUpdatePage(driver)
        update.click_update_firmware()
        update.ping_server()

if __name__ == "__main__":
    unittest.main()

