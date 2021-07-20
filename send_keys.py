import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class ejercicio_keys(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")

	def test_autom(self):
		driver = self.driver
		driver.get("http://opencart.abstracta.us/index.php?route=common/home")
		time.sleep(3)
		busqueda = driver.find_element_by_name("search")
		busqueda.send_keys("iphone")
		time.sleep(1)
		busqueda.send_keys(Keys.ENTER)
		time.sleep(2)

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()