import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver

class usando_unittest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")


	def test_manejando_ventanas(self):
		driver = self.driver
		driver.get("https://google.com/intl/es/gmail/about/#")
		siguiente_pag = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/ul[1]/li/div/div/div[1]/div/div[3]/a[1]")
		siguiente_pag.click()
		print(driver.current_window_handle)
		driver.implicitly_wait(2)
		handles = driver.window_handles 
		for handle in handles:
			driver.switch_to.window(handle)
			print(driver.title)


	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()
