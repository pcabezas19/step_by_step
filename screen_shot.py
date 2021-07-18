from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")
driver.get('https://www.amazon.es/')
driver.get_screenshot_as_file("C:\\Users\\thepa\\Desktop\\curso\\Testing 2021\\nombre_que_quiero.png")

driver.quit()