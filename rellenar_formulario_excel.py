from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook

driver = webdriver.Chrome(executable_path = r"C:\dchrome/chromedriver.exe")
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdYwJbkNLf3GfepoiOBgkXLhrHBoYR8xqWgl3ZmsqRVSeCxFA/viewform")
time.sleep(3)
filesheet ="./formulario_excel.xlsx"
hojas = wb.get_sheet_names()
print(hojas)
nombre_hojas = wb.get_sheet_by_name("Hoja1_ejecutada")
wb.close()

for i in range(1,5):
	nomb, apell, edad = nombre_hojas[f'A{i}:C{i}'][0]
	print(nomb.value, apell.value, edad.value)
	driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(nomb.value)
	driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(apell.value)
	driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(str(edad.value))
	driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div/div/span/span").click()
	driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[4]/a").click()

driver.quit()