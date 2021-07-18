import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class varias_pestanias(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")

	def test_practic(self):
		driver = self.driver
		driver.get("https://www.google.com.ar")
		time.sleep(2)
		driver.execute_script("window.open('');")
		time.sleep(2)
		driver.switch_to.window(driver.window_handles[1])
		driver.get("https://www.selenium.dev")
		time.sleep(2)
		driver.switch_to.window(driver.window_handles[0])
		time.sleep(2)

if __name__ == '__main__':
	unittest.main()


		