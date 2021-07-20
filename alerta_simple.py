from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")
driver.get("file:///C:/Users/thepa/Desktop/curso/Testing%202021/html%20de%20alerts/alert_simple.html")
time.sleep(3)
alertando = driver.find_element_by_name("alert")
alertando.click()
time.sleep(3)
alertando=driver.switch_to_alert()
alertando.dismiss()
time.sleep(3)

driver.quit()