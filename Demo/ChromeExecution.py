from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# chrome_options = webdriver.ChromeOptions()
chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disbale-extensions")

driver = webdriver.Chrome()
driver.set_page_load_timeout(10)
driver.get("https://google.com")
textbox = driver.find_element(By.NAME, 'q')
textbox.send_keys("Automation step by step....")
searchBtn = driver.find_element(By.NAME,'btnK')
searchBtn.click()

print(driver.title)
driver.close()
driver.quit()

print("Test Completed")
