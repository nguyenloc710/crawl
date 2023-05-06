from selenium import webdriver
from selenium.webdriver.chrome.service import Service

print("start")
options = webdriver.ChromeOptions()
options.headless = True

service = Service("/home/ubuntu/driveSelenium/chromedriver")
driver = webdriver.Firefox(options=options, service=service)
print("done drive")

# Navigate to a webpage
driver.get('https://www.google.com')

# Quit the webdriver
driver.quit()
