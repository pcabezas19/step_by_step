import HtmlTestRunner
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



class suite(unittest.TestCase):
	def setUp(self):
		
		self.driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")

	def test_1busqueda(self):
		driver = self.driver
		driver.get("http://www.google.com")
		time.sleep(1)
		busqueda = driver.find_element_by_name("q")
		busqueda.send_keys("selenium")
		busqueda.submit()
		time.sleep(1)

	def test_2scrollDown(self):
		driver = self.driver	
		driver.get("https://www.amazon.es")
		time.sleep(1)
		driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
		time.sleep(1)

	def test_3radio_button(self):
		driver = self.driver
		driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
		time.sleep(1)
		radiob = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/input[4]")
		radiob.click()
		time.sleep(2)
		tc=driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/input[3]")
		tc.click()
		time.sleep(2)

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output = 'Resultado_Testplan'))