import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options#para hacer el guardado de la descarga en la carpeta que quiero
import time


class buscar_frame(unittest.TestCase):
	def setUp(self):
		chromeOptions = Options()
		chromeOptions.add_experimental_option("prefs", {
			"download.default_directory":"C:\\Users\\thepa\\Desktop\\curso\\Testing 2021"})#para guardar en la carpeta que quiero y no directo en la de descargas
		self.driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe", chrome_options = chromeOptions)

	def test_frame(self):
		driver = self.driver
		driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download")
		time.sleep(2)#en este caso como hay dos frames (o sea dos paginas embebidas en una, hago primero switch a donde esta mi click y luego hago click a lo que quiero descargar)
		driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[7]/div[4]/div/div/iframe"))#primero switchamos a la otra pagina con full xpath
		time.sleep(3)
		driver.find_element_by_xpath("/html/body/p[2]/a/img").click()# ya en el frame que es, le doy cick a lo que quiero descargar
		time.sleep(3)

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()


		
		
		
		
