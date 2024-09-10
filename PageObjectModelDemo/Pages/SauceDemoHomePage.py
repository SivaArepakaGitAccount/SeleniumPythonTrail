from selenium.webdriver.common.by import By
from PageObjectModelDemo.Locators.objectlocators import Locators

class SauceDemoHomePage():

    # creating constructor
    def __init__(self, driver):
        self.driver = driver

        self.username_link = Locators.username_link
        self.logout_link = Locators.logout_link

    def click_usernamelink(self):
        self.driver.find_element(By.ID,self.username_link).click()

    def click_logoutlink(self):
        self.driver.find_element(By.ID,self.logout_link).click()