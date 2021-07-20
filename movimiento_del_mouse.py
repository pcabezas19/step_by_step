import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains #controla las funciones del mouse, dar permiso para dar los clicks
import time

#esto sirve para hacer movimientos de mouse paso aposo
class ejerciciode_del_mouse(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")

	def test_mouse(self):
		driver = self.driver
		driver.get("http://opencart.abstracta.us/")
		time.sleep(3)
		movimiento_mouse = driver.find_element_by_xpath("//*[@id='menu']/div[2]/ul/li[3]/a")#este es el que elige a donde vamos
		movimiento_mouse2 = driver.find_element_by_xpath("//*[@id='menu']/div[2]/ul/li[3]/div/div/ul/li[2]/a") #este elige lo que queremos dentro del menú que tenemos
		moverse = ActionChains(driver)#con esto le dice que haga un actionschains en el driver y se guarde en la variable moverse
		moverse.move_to_element(movimiento_mouse).move_to_element(movimiento_mouse2).click().perform() #esta es la ActionChains que hace mover el mouse a donde queremos. Debemos darle paso a paso por donde pasa
		#perfomr() significa ejecutalo ya
		time.sleep(3)

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()