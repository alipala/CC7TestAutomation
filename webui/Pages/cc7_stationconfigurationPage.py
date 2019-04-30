from webui.Locators.locators import Locators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class StationConfigurationPage:

    def __init__(self, driver):
        self.driver = driver
        self.dropdown_process_access_id = Locators.dropdown_process_access_id
        self.station_configuration_linktext = Locators.station_configuration_linktext
        self.station_name_textbox_xpath = Locators.station_name_textbox_xpath
        self.add_button_id = Locators.add_button_id
        self.confirm_window_xpath = Locators.confirm_window_xpath
        self.s7_tab_link_xpath = Locators.s7_tab_link_xpath
        self.ip_address_textbox_id = Locators.ip_address_textbox_id
        self.controller_family_id = Locators.controller_family_id
        self.save_button_xpath = Locators.save_button_xpath
        self.apply_button_id = Locators.apply_button_id

    def nav_station_configuration_page(self):
        self.driver.find_element_by_id(self.dropdown_process_access_id).click()
        self.driver.find_element_by_link_text(self.station_configuration_linktext).click()

    def enter_station_name(self, station_name):
        self.driver.find_element_by_xpath(self.station_name_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.station_name_textbox_xpath).send_keys(station_name)

    def add_station(self):
        self.driver.find_element_by_id(self.add_button_id).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.confirm_window_xpath))).click()

    def navigate_to_s7(self):
        self.driver.find_element_by_xpath(self.s7_tab_link_xpath).click()

    def enter_ip_address(self, ip_address):
        self.driver.find_element_by_id(self.ip_address_textbox_id).clear()
        self.driver.find_element_by_id(self.ip_address_textbox_id).send_keys(ip_address)

    def select_controller_family(self):
        controller = Select(self.driver.find_element_by_id(self.controller_family_id))
        controller.select_by_value("S7-1200/1500")

    def click_save(self):
        self.driver.find_element_by_xpath(self.save_button_xpath).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.confirm_window_xpath))).click()

    def apply_changes(self):
        self.driver.find_element_by_id(self.apply_button_id).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.confirm_window_xpath))).click()
