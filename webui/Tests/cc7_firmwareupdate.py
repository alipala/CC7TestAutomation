import unittest
import time
import sys
import os
sys.path.append((os.path.join(os.path.dirname(__file__), "..", "..")))
from webui.Pages.cc7_loginPage import LoginPage
from webui.Pages.cc7_homePage import HomePage
from webui.Pages.cc7_firmwareupdatePage import FirmwareUpdatePage
from webui.Base.cc7_base import TestBase

class FirmwareUpdateTest(TestBase):

    def test_01_login(self):
        driver = self.driver
        driver.get("https://192.168.3.55")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("CloudConnect_7")
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

