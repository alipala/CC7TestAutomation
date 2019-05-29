import time
import unittest
import sys
import os
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from webui.Pages.cc7_loginPage import LoginPage
from webui.Pages.cc7_homePage import HomePage
from webui.Base.cc7_base import TestBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class LoginTest(TestBase):

    __server_ip_address = "https://192.168.3.55"
    __user_data_file = r"\login_details.xlsx"

    def test_01_login_validation(self):
        driver = self.driver
        self.df = pd.read_excel(os.getcwd() + self.__user_data_file)
        driver.get(self.__server_ip_address)
        login = LoginPage(driver)
        for index, row in self.df.iterrows():
            login.enter_username(row["username"])
            login.enter_password(row["pass"])
            login.click_login()

            homepage = HomePage(driver)
            time.sleep(2)
            #homepage.click_logout()

if __name__ == "__main__":
    unittest.main()
