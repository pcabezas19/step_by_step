from selenium import webdriver
import keyboard
import pyautoguie
import time


driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")
driver.get("http://217.182.87.241/testlink/login.php")
time.sleep(2)
keyboard.write("lo que quiero escribir")
pyautogui.press("tab")
keyboard.write("en este caso la clave")
pyautogui.press("enter")
driver.close()
