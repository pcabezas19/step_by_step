from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")
driver.get("file:///C:/Users/thepa/Desktop/curso/Testing%202021/html%20de%20alerts/promp_alert.html")
time.sleep(3)
boton = driver.find_element_by_name("prompt_alert")
boton.click()
time.sleep(2)
boton = driver.switch_to_alert()


driver.quit()
