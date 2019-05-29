from webui.Locators.locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.logout_button_xpath = Locators.logout_button_xpath
        self.dropdown_datapoints_xpath = Locators.dropdown_datapoints_xpath
        self.dropdown_item_datapoints_xpath = Locators.dropdown_item_datapoints_xpath
        self.logout_confirm_xpath = Locators.logout_confirm_xpath

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_button_xpath).click()
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.logout_confirm_xpath))).click()


