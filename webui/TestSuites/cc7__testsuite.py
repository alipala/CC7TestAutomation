import unittest
from webui.Tests.cc7_login import LoginTest
from webui.Tests.cc7_stationconfiguration import StationConfigurationTest
from webui.Tests.cc7_firmwareupdate import FirmwareUpdateTest
import HtmlTestRunner
import os

# get all tests from SearchText and HomePageTest class
login_test = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
station_configuration_test = unittest.TestLoader().loadTestsFromTestCase(StationConfigurationTest)
firmware_update_test = unittest.TestLoader().loadTestsFromTestCase(FirmwareUpdateTest)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([firmware_update_test])


runner = HtmlTestRunner.HTMLTestRunner(output="D:/CC7TestAutomation/webui/Reports")
runner.run(test_suite)


# if __name__ == "__main__":
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(verbosity=2, output="D:/CC7TestAutomation/webui/Reports")).runTests(test_suite)

