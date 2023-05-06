from selenium import webdriver
from selenium.webdriver.firefox.service import Service

print("start")
binary = '/usr/bin/firefox'
options = webdriver.FirefoxOptions()
options.headless = True

service = Service("/home/ubuntu/driveSelenium/geckodriver")
driver = webdriver.Firefox(firefox_binary=binary, options=options, service=service)
print("done drive")

# Navigate to a webpage
driver.get('https://www.google.com')

# Quit the webdriver
driver.quit()
