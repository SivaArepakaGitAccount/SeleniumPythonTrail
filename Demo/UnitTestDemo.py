import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        # implicit wait implementation This waits the time specified by default
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_googlesearchvalid(self):
        self.driver.get("https://google.com")
        textbox = self.driver.find_element(By.NAME, 'q')
        textbox.send_keys("Automation step by step")
        searchBtn = self.driver.find_element(By.NAME, 'btnK')
        # explicit wait
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.element_to_be_clickable(searchBtn))
            print("Search button is clickable")
        except:
            print("Search button is not clickable")
            exit(1)
        searchBtn.click()
        print(self.driver.title)
        self.assertEqual(self.driver.title, "Automation step by step - Google Search")

    def test_googlesearchinvalid(self):
        self.driver.get("https://google.com")
        textbox = self.driver.find_element(By.NAME, 'q')
        textbox.send_keys("Siva")
        searchBtn = self.driver.find_element(By.NAME, 'btnK1')
        searchBtn.click()
        print(self.driver.title)
        self.assertEqual(self.driver.title, "Siva - Google Search")

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner
    (output='C:/Users/Sivakumar.Arepaka/Videos/Python/Selenium/Reports'))

    # execute the tests in specific order
    # suite = unittest.TestSuite()
    # suite.addTest(MyTestCase('test_googlesearchvalid'))
    # suite.addTest(MyTestCase('test_googlesearchinvalid'))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
