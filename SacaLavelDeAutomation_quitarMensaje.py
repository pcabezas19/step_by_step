import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class ejercicio_keys(unittest.TestCase):
	def setUp(self):
		chrome_options_pedro = webdriver.ChromeOptions()
		chrome_options_pedro.add_experimental_option("excludeSwitches",['enable-automation'])
		self.driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe", options = chrome_options_pedro)
	def test_autom(self):
		driver = self.driver
		driver.get("http:www.google.com")
		time.sleep(3)

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()