import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By #para send.keys
import time

class ejercicio_subir_archivo(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")

	def test_subir(self):
		driver = self.driver
		driver.get("https://mdbootstrap.com/docs/standard/plugins/file-upload/")
		time.sleep(2)
		#busco a donde voy a mandar y con el send_keys le digo donde esta lo que va a subir, copio la direccion y mando el archivo
		mover = driver.find_element_by_id("input-file-now").send_keys("C:\\Users\\thepa\\Pictures\\ERN.jpg")#doble slash \\ para que no tome las palabras reservadas
		time.sleep(10)

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()

