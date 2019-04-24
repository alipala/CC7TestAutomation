from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import selenium.common.exceptions
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="D:/CC7TestAutomation/webui/drivers/chromedriver.exe")

class Login:
    def __init__(self):
        print("object is initialized")
        driver.maximize_window()
    def connect(self):
        try:
            driver.get('https://192.168.3.89')
            assert "Simatic Cloud Connect" in driver.title
            userName = driver.find_element_by_name('ccUsername')
            userName.send_keys("Admin")
            passWord = driver.find_element_by_name('ccPassword')
            passWord.send_keys("CloudConnect_7")
            saveButton = driver.find_element_by_xpath("//button[@type='submit'][contains(.,'Log in')]")
            saveButton.submit()
            time.sleep(5)
        except selenium.common.exceptions.NoSuchElementException:
            assert "No results found." not in driver.page_source
        finally:
            print("TODO")

class InterfaceConfig:
    def __init__(self):
        print("InterfaceConfig class called")
    def nav_interface_config(self):
        driver.find_element_by_xpath("//a[@class='nav-link dropdown-toggle'][contains(.,'Interface configuration')] ").click()
        driver.find_element_by_xpath("//a[@class='dropdown-item'][contains(.,'Ethernet')]").click()

        if driver.find_element_by_id("ccCloudIP4").get_attribute("checked"):
            print("IP4 is already enabled")
        else:
            driver.find_element_by_xpath('//*[@id="ccIfaceCfgForm"]/div[8]/div/div/label').click()
        time.sleep(5)

        #TODO
        # if driver.find_element_by_id("ccCloudIP4Dhcp").get_attribute("checked"):
        #     driver.find_element_by_id("ccCloudIP4Dhcp").click()
        driver.find_element_by_id("ccCloudIP4Address").clear()
        driver.find_element_by_id("ccCloudIP4Address").send_keys("192.168.3.97")
        driver.find_element_by_id("ccCloudIP4Subnet").clear()
        driver.find_element_by_id("ccCloudIP4Subnet").send_keys("255.255.255.0")

        save_btn = driver.find_element_by_xpath("//button[@type='submit'][contains(.,'Save')]")
        save_btn.submit()

        time.sleep(2)
        driver.find_element_by_id('ccConfirmWindowN').click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        apply_btn = driver.find_element_by_id("ccApply")
        apply_btn.click()

        wait = WebDriverWait(driver, 15)
        element = wait.until(EC.visibility_of_element_located((By.ID, 'ccConfirmWindowN')))
        driver.find_element_by_id('ccConfirmWindowN').click()

class DataPoint:
    def __init__(self):
        print("DataPoint class called")
        self.offset_list = [0,1,2,4,6,10,18,20,22,26,34,36,38,42,50,54,62,70,82]

    def nav_datapoints(self):
        time.sleep(3)
        driver.find_element_by_xpath("//a[@class='nav-link dropdown-toggle'][contains(.,'Data points')]").click()
        driver.find_element_by_xpath("//a[@class='dropdown-item'][contains(.,'Data points')]").click()


    def add_data_point(self):
        offset_value = 338
        data_count = 0
        for item in range(0,500):
            driver.find_element_by_id("ccDataAdd").click() #Add data point
            Select(driver.find_element_by_xpath('//*[@id="ccData"]/table/tbody/tr[2]/td[3]/select')).select_by_index(2) #Target
            driver.find_element_by_xpath('//*[@id="ccData"]/table/tbody/tr[2]/td[4]/input').send_keys("var{0}".format(item)) #Data point name
            Select(driver.find_element_by_xpath('//*[@id="ccData"]/table/tbody/tr[2]/td[6]/select')).select_by_index(3) #Area
            driver.find_element_by_xpath('//*[@id="ccData"]/table/tbody/tr[2]/td[7]/input').send_keys("1") #DB No
            if item == 0:
                driver.find_element_by_xpath('//*[@id="ccData"]/table/tbody/tr[2]/td[8]/input').send_keys('0.0') #Offset for Boolen type
            elif 0 < item < 18:
                Select(driver.find_element_by_xpath('//*[@id="ccData"]/table/tbody/tr[2]/td[5]/select')).select_by_index(item)  # Data type
                driver.find_element_by_xpath('//*[@id="ccData"]/table/tbody/tr[2]/td[8]/input').send_keys(self.offset_list[item])  # Offset for 0 > item > 19
                if item == 18 and driver.find_element_by_xpath('//*[@id="ccData"]/table/tbody/tr[2]/td[9]/input').is_enabled():
                    driver.find_element_by_xpath('//*[@id="ccData"]/table/tbody/tr[2]/td[9]/input').send_keys("254")
            else:
                Select(driver.find_element_by_xpath('//*[@id="ccData"]/table/tbody/tr[2]/td[5]/select')).select_by_index(11)  # Data type
                driver.find_element_by_xpath('//*[@id="ccData"]/table/tbody/tr[2]/td[8]/input').send_keys(offset_value)  # Offset
                offset_value += 2

            Select(driver.find_element_by_xpath('//*[@id="ccData"]/table/tbody/tr[2]/td[10]/select')).select_by_index(2) #Read/Write
            data_count += 1
            if data_count == 49:
                print(data_count)
                driver.find_element_by_xpath("/html/body/main/div/form/button[3]").submit()  # Click Save
                wait = WebDriverWait(driver, 15)
                element = wait.until(EC.visibility_of_element_located((By.ID, 'ccConfirmWindowN')))  # Confirm Popup
                driver.find_element_by_id('ccConfirmWindowN').click()
                data_count = 0
                print(data_count)
                continue

        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ccApply"]').click() #Apply changes
        wait = WebDriverWait(driver, 15)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ccConfirmWindowN"]'))) #Confirm Popup
        driver.find_element_by_xpath('//*[@id="ccConfirmWindowN"]').click()


class RunTest:
    login = Login()
    login.connect()
    # config = InterfaceConfig()
    # config.nav_interface_config()
    # data_point = DataPoint()
    # data_point.nav_datapoints()
    # data_point.add_data_point()