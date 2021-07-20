from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")
driver.get("file:///C:/Users/thepa/Desktop/curso/Testing%202021/html%20de%20alerts/confirm_alert.html")#hecho en html den mi maquina
time.sleep(3)
variable_confirmAlert = driver.find_element_by_name("confirm_alert")
variable_confirmAlert.click()
time.sleep(3)
variable_confirmAlert=driver.switch_to_alert()
variable_confirmAlert.accept()

driver.close()