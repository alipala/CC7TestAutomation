import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from webui.Pages.cc7_loginPage import LoginPage
from webui.Pages.cc7_homePage import HomePage
from webui.Base.cc7_base import TestBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class LoginTest(TestBase):

    def test_01_login_validation(self):
        driver = self.driver
        driver.get("https://192.168.3.89")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("CloudConnect_7")
        login.click_login()

        homepage = HomePage(driver)
        time.sleep(5)
        homepage.click_logout()
        time.sleep(2)
        wait = WebDriverWait(driver, 15)
        element = wait.until(EC.visibility_of_element_located((By.ID, 'ccConfirmWindowN')))  # Confirm Popup
        driver.find_element_by_id('ccConfirmWindowN').click()

if __name__ == "__main__":
    unittest.main()
