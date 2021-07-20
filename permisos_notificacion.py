from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

opciones = Options()
opciones.add_experimental_option("prefs",{"profile.default_content_setting_values.notifications" : 1})
driver = webdriver.Chrome(chrome_options = opciones, executable_path = r"C:\dchrome\chromedriver.exe")
driver.get("Ingresar una pagina que tenga la pantalla emergente de permitir notificac")
time.sleep(3)

driver.quit()