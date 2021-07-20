import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class click_derecho (unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")

	def test_clickDerecho(self):
		driver = self.driver
		driver.get("http://opencart.abstracta.us")
		time.sleep(3)
		click_derecho = driver.find_element_by_xpath("//*[@id='menu']/div[2]/ul/li[1]/a")
		acciones = ActionChains(driver)#aca le digo que tomara el doble click en la variable acciones
		acciones.context_click(click_derecho).perform()#aca estoy haciendo el click derecho  en el boton avisado en el xpath
		time.sleep(3)

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()