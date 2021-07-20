from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")
driver.get("https://www.w3schools.com/html/html_tables.asp")
time.sleep(3)
tabla = driver.find_element_by_xpath("//*[@id='customers']/tbody/tr[3]/td[1]").text
print(tabla)
fila = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr"))
colum = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[1]/th"))
print(fila)
print(colum)
for n in range(2,fila+1): 
	for i in range(1,colum+1):
		variable_nueva = driver.find_element_by_xpath("//*[@id='customers']/tbody/tr["+str(n)+"]/td["+str(i)+"]").text
		print(variable_nueva, end='     ')
	print()

driver.quit()