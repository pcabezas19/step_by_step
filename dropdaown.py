from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")

driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
desplegar = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select")#primero lo conseguimos el desplegable
desplegue = driver.find_elements_by_tag_name("option")#segundo lo capturamos(pero si queremos un for)
time.sleep(2)

'''for option in desplegue:#esto lo hacemos si queremos que lo recorra, sino no hace fata /// creo que esto no estaba andando
	option.click()
	time.sleep(1)'''

seleccion = Select(driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select"))#tercero le metemos el select a la lista que conseguimos con el xpath u otro find_element
seleccion.select_by_value("4")#el valor atajado, le ponemos cual de todos en el desplegable es el que queremos
#tambien puede se .select_by_index(4) (numero sin las comillas) o .select_by_visible_text("xxxx")
time.sleep(4)

driver.quit()