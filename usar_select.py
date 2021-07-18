import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

class practicando_Select(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")

	def test_usarSelect(self):
		driver = self.driver
		driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
		time.sleep(3)
		select = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select")
		opciones = select.find_elements_by_tag_name("option")
		time.sleep(3)

		for option in opciones:
			print("los valores son: %s"% option.get_attribute("value"))
			time.sleep(1)
		seleccionando = Select(driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select"))
		seleccionando.select_by_value("10")
		time.sleep(3)

if __name__ == '__main__':
		unittest.main()	



