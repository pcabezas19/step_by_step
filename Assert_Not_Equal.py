import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class usando_unittest(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")

	def test_1assertNotEqual(self):
		driver = self.driver
		driver.get("https://www.Google.com/")
		titulo_pagina = driver.title 
		self.assertNotEqual("Google",titulo_pagina,"Titulo igual mmg")

	def test_2case(self):
		driver = self.driver
		driver.get("https://www.Google.com/")
		variable = driver.find_element_by_name("q")
		variable.send_keys("hola")
		variable.submit()
		time.sleep(3)

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()
