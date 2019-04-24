from webui.Locators.locators import Locators

class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.logout_button_id = Locators.logout_button_id
        self.dropdown_datapoints_xpath = Locators.dropdown_datapoints_xpath
        self.dropdown_item_datapoints_xpath = Locators.dropdown_item_datapoints_xpath

    def click_logout(self):
        self.driver.find_element_by_id(self.logout_button_id).click()
