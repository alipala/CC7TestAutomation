from webui.Locators.locators import Locators

class DataPoints():

    def __init__(self, driver):
        self.driver = driver


    def click_data_points(self):
        self.driver.find_element_by_xpath(self.dropdown_datapoints_xpath).click()
        self.driver.find_element_by_xpath(self.dropdown_item_datapoints_xpath).click()



