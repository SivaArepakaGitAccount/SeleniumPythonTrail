import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.NAME,'username').send_keys("admin")
driver.find_element(By.NAME, 'password').send_keys("admin123")
driver.find_element(By.XPATH, "//button[text()=' Login ']").click()

time.sleep(10)
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/i').click()
driver.find_element(By.XPATH,"//*[text()='Logout']").click()

time.sleep(2)
driver.close()
driver.quit()
print("Test execution completed")