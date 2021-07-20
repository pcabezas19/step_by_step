from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")
driver.get("C:\\Users\\thepa\\Desktop\\curso\\Testing 2021\\fromulario.html")#html hecho por kasiel99 y txt datos,formulario.
time.sleep(3)

#iniciar ciclon de autollenado de formulario

with open ('datos_formulario.txt') as file:
		for i, line in enumerate(file):
			usuario = (line)
			separado = "," #separado por comas lo que esta dentro del archivo
			dividir = usuario.split(separado)
			try:
				gotdata = dividir[1]
				dominio = dividir[0]
				anio = dividir [1]
			except IndexError:
				gotdata = 'null'
#################################hasta acá la parte de meter y sacar data del txt#################################################

			print(dominio)
			print(anio)
			driver.find_element_by_id("login").send_keys(dominio)
			time.sleep(2)
			driver.find_element_by_id("cont").send_keys(anio)
			time.sleep(2)
			driver.find_element_by_xpath("/html/body/p[2]/input[2]").click()
			time.sleep(2)

file.close()
driver.close()