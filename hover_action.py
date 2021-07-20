from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")
driver.get("https://www.google.com.ar")
time.sleep(3)
elem = driver.find_element_by_link_text("Condiciones")
hover = ActionChains(driver).move_to_element(elem) 
hover.perform()

