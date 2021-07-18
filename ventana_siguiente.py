import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class ejercicio_adelante_atras(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")

	def test_ejercicio(self):
		driver = self.driver
		driver.get("https://nu.com.ar/")
		time.sleep(2)
		driver.get("https://www.uala.com.ar/")
		time.sleep(2)
		driver.get("https://www.brubank.com/")
		time.sleep(2)
		driver.back()
		time.sleep(5)
		driver.back()
		time.sleep(2)
		driver.forward()

if __name__ == '__main__':
	unittest.main()