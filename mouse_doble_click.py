import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains #para tener acceso a dispositivo de hardware
import time


'''este script subraya con doble click la palabra que quiero, la consigo con xpath y puedo con otro script despues copiarla o lo que necesite'''
class ejercicio_mouse(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")

	def test_doble_click(self):
		driver = self.driver
		driver.get("https://www.google.com/search?q=suerte&rlz=1C1CHBF_esAR915AR915&oq=suerte&aqs=chrome..69i57j46j0i175i199j0l2j0i131i433j0l2j46j0.3266j0j4&sourceid=chrome&ie=UTF-8")
		time.sleep(4)
		doble_click = driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div/div/div[2]/div[1]/span/em")# xpath
		actions = ActionChains(driver)
		actions.double_click(doble_click).perform()#le estoy diciendo que a la variable doble_click, guardada en la variable actions, le de doble click con actions.double_click. Con perform()hago que se ejecute
		time.sleep(3)

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()

