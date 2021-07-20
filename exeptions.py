#haré un exeption para un radio button, pero esta es la sintaxis de exception en general
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

class haciendo_exeptions(unittest.TestCase):
	def setUp(self):
		self.driver= webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")

	def test_exeption(self):
		driver = self.driver
		driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
		time.sleep(2)
		rd_button = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/input[4]")
		time.sleep(2)
		try:
			rd_button.click()
			time.sleep(3)
		except Exception as e:#la letra e es de exception
			print("no se ejecutó e evento del click")#trae cuando es falso
			print(e)#trae cuando es verdadero
			time.sleep(2)

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()



