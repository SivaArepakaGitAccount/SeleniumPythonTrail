import time
import unittest
import sys
import os
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from PageObjectModelDemo.Pages.SauceDemoLoginPage import SauceDemoLoginPage
from PageObjectModelDemo.Pages.SauceDemoHomePage import SauceDemoHomePage


class SauceDemoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        # implicit wait implementation This waits the time specified by default
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def testSauceDemoLogin(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.NAME, 'user-name').send_keys("standard_user")
        self.driver.find_element(By.NAME, 'password').send_keys("secret_sauce")
        self.driver.find_element(By.ID, 'login-button').click()

        # wait = self.driver.WebDriverWait(10)
        # wait.until(EC.element_to_be_clickable(self.driver.find_element(By.ID, 'react-burger-menu-btn')))

        time.sleep(2)
        self.driver.find_element(By.ID, 'react-burger-menu-btn').click()
        self.driver.find_element(By.ID, 'logout_sidebar_link').click()
        time.sleep(2)

    def testSauceDemoLoginPageObject(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")

        loginpage = SauceDemoLoginPage(driver)
        loginpage.enter_username("standard_user")
        loginpage.enter_password("secret_sauce")
        loginpage.click_loginbutton()

        # wait = self.driver.WebDriverWait(10)
        # wait.until(EC.element_to_be_clickable(self.driver.find_element(By.ID, 'react-burger-menu-btn')))
        homepage = SauceDemoHomePage(driver)
        time.sleep(2)
        homepage.click_usernamelink()
        homepage.click_logoutlink()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

print("Test execution completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Sivakumar.Arepaka/Videos/Python/Selenium/Reports'))