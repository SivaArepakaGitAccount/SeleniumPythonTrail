import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--headless")
# firefox_options.add_argument("--disbale-extensions")

fireFoxDriver = webdriver.Firefox(firefox_options)
fireFoxDriver.set_page_load_timeout(100)
fireFoxDriver.get("https://google.com")
textbox = fireFoxDriver.find_element(By.NAME, 'q')
textbox.send_keys("Automation step by step")
searchBtn = fireFoxDriver.find_element(By.NAME,'btnK')
time.sleep(2)
searchBtn.click()

print(fireFoxDriver.title)
fireFoxDriver.close()
fireFoxDriver.quit()

print("Test Completed")
