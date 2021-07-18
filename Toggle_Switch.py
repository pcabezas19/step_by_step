import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class ejercicio_toggle(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")

	def test_toggle(self):
		driver = self.driver
		driver.get("https://www.w3schools.com/howto/howto_css_switch.asp")
		time.sleep(2)
		toggle = driver.find_element_by_xpath("//*[@id='main']/label[3]/div")
		toggle.click()
		time.sleep(2)
		toggle.click()
		time.sleep(2)

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()
