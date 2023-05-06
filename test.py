from selenium import webdriver
from selenium.webdriver.firefox.service import Service

print("start")
# options = FirefoxOptions()
# options.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe'
# driver = webdriver.Firefox(options=options, executable_path="D:\drive\geckodriver.exe")
options = webdriver.FirefoxOptions()
options.headless = True

service = Service("/snap/bin/geckodriver")
driver = webdriver.Firefox(options=options, service=service)
print("done drive")

# Navigate to a webpage
driver.get('https://www.google.com')

# Quit the webdriver
driver.quit()
