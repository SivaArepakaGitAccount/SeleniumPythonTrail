import time

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

edge_options = Options()
edge_options.add_argument("--headless")
#driver = webdriver.Edge()
driver = webdriver.Edge(edge_options)
driver.set_page_load_timeout(10)

driver.get("https://google.com")
print(driver.title)

textbox = driver.find_element(By.NAME, 'q')
textbox.send_keys("Automation step by step....")
searchBtn = driver.find_element(By.NAME,'btnK')
time.sleep(2)
searchBtn.click()
driver.close()
driver.quit()

print("Test Completed")