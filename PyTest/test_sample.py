import sys
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestSample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        time.sleep(2)
        driver.close()
        driver.quit()

    def test_login(self, test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME, 'username').send_keys("admin")
        driver.find_element(By.NAME, 'password').send_keys("admin123")
        driver.find_element(By.XPATH, "//button[text()=' Login ']").click()
        time.sleep(10)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/i').click()
        driver.find_element(By.XPATH, "//*[text()='Logout']").click()

    # this test will be skipped for this build only
    @pytest.mark.skip(reason="Skipped for this build")
    def test_loginskip(self, test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME, 'username').send_keys("admin")
        driver.find_element(By.NAME, 'password').send_keys("admin123")
        driver.find_element(By.XPATH, "//button[text()=' Login ']").click()
        time.sleep(10)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/i').click()
        driver.find_element(By.XPATH, "//*[text()='Logout']").click()

    # this test will be skipped if the pycharm version < 3.6
    @pytest.mark.skipif(sys.version_info < (3,6), reason="Skipped for this build")
    def test_loginskipif(self, test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME, 'username').send_keys("admin")
        driver.find_element(By.NAME, 'password').send_keys("admin123")
        driver.find_element(By.XPATH, "//button[text()=' Login ']").click()
        time.sleep(10)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/i').click()
        driver.find_element(By.XPATH, "//*[text()='Logout']").click()

    # this test will be executed on windows OS only
    @pytest.mark.windows
    def test_login_windows(self, test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME, 'username').send_keys("admin")
        driver.find_element(By.NAME, 'password').send_keys("admin123")
        driver.find_element(By.XPATH, "//button[text()=' Login ']").click()
        time.sleep(10)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/i').click()
        driver.find_element(By.XPATH, "//*[text()='Logout']").click()

    # this test will be executed on mac OS only
    @pytest.mark.mac
    def test_login_mac(self, test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME, 'username').send_keys("admin")
        driver.find_element(By.NAME, 'password').send_keys("admin123")
        driver.find_element(By.XPATH, "//button[text()=' Login ']").click()
        time.sleep(10)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/i').click()
        driver.find_element(By.XPATH, "//*[text()='Logout']").click()
