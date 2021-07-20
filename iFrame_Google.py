import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
'''un frame es una pagina embebida en otra pagina, aca lo que haré será buscar en la pagina de Google las aplicaciones y como es como ver
una pagina dentro de otra, primero le voy a agarrar su id a la hamburguesa de aplicaciones y luego el xpath para tomar la app que quiero'''

class buscar_frame(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")

	def test_frame(self):
		driver = self.driver
		driver.get("https://www.google.com/")
		time.sleep(2)
		cliquear1 = driver.find_element_by_id("gbwa")
		time.sleep(2)
		cliquear1.click()
		time.sleep(3)
		#pasos: debemos si o si cambiar de frame, hago eso con switch, para eso busco la info del frame y luego con eso es que puedo trabajar como si estuviera subido en ese frame
		#hay que conseguir donde se hubica ese iframe para que switchee correctame
		driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div[3]/iframe"))#lo conseguí en incognito
		time.sleep(3)
		cliquear2 = driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/c-wiz/div/div/ul[1]/li[4]/a/div/span")
		cliquear2.click()
		time.sleep(3)

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()

#primero debo usar el xpath del frame y luego el xpath de lo que quiero tocar dentro del frame.