from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")
driver.get("https://www.google.com.ar")
time.sleep(3)
displayelemen = driver.find_element_by_name("btnI")
print(displayelemen.is_displayed())
print(displayelemen.is_enabled())
driver.quit()