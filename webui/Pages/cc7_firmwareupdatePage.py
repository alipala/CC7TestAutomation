from webui.Locators.locators import Locators
import os
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class FirmwareUpdatePage:

    def __init__(self, driver):
        self.__cc7filename = "/6GK1 411-5AC00 T00.01.99.upd"
        self.driver = driver
        self.dropdown_maintenance_id = Locators.dropdown_maintenance_id
        self.maintenance_linktext = Locators.maintenance_linktext
        self.firmware_file_input_id = Locators.firmware_file_input_id
        self.update_firmware_button_id = Locators.update_firmware_button_id
        self.firmware_update_confirm_window = Locators.firmware_update_confirm_window
        self.confirm_window_xpath = Locators.confirm_window_xpath

    def nav_maintenance_page(self):
        self.driver.find_element_by_id(self.dropdown_maintenance_id).click()
        self.driver.find_element_by_link_text(self.maintenance_linktext).click()

    def browse_firmware_file(self):
        self.driver.find_element_by_id(self.firmware_file_input_id).send_keys(os.getcwd() + self.__cc7filename)

    def click_update_firmware(self):
        self.driver.find_element_by_id(self.update_firmware_button_id).click()

        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.firmware_update_confirm_window))).click()
            print("Page is ready...")
        except TimeoutException:
            print("Loading took too much time:", self.firmware_update_confirm_window)

    def ping_server(self):
        cc7_server = "https://192.168.3.89"

        response = os.system("ping -t" + cc7_server)
        if response == 0:
            ping_status = cc7_server, "is up!"
        else:
            ping_status = "Failed with", response

        return ping_status






