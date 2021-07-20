from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path = r'C:\dchrome\chromedriver.exe')
driver.get('https://www.amazon.es/')
time.sleep(3)
all_cookies = driver.get_cookies()
print(all_cookies)

driver.quit()