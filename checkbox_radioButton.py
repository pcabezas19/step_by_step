import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class ejercicio_radiobutton_checkbox(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")

	def test_ejercicio(self):
		driver = self.driver
		driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
		time.sleep(3)
		radiob = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/input[4]")
		radiob.click()
		time.sleep(2)
		tc=driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/div[3]/div[1]/input[4]")
		tc.click()
		time.sleep(2)

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()
