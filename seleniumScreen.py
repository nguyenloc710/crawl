import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.service import Service

def screenShotVideoYT(id,times):
    # options = FirefoxOptions()
    # options.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe'
    # driver = webdriver.Firefox(options=options, executable_path="D:\drive\geckodriver.exe")
    options = webdriver.FirefoxOptions()
    options.headless = True

    service = Service("/snap/bin/geckodriver")
    driver = webdriver.Firefox(options=options, service=service)
    url = "https://www.youtube.com/embed/"+id+"?start="+str(times)
    # driver.get("https://www.youtube.com/watch?v=NXcR7fgo7vE&t=60s")
    driver.get(url)
    print("OK")
    driver.find_element(By.TAG_NAME, "video")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".ytp-progress-bar-container"))
    )
    time.sleep(2)
    driver.execute_script("document.getElementsByTagName('video')[0].click()")
    time.sleep(2)
    driver.execute_script("""
            (function (window, document) {
             var canvas = document.createElement('canvas');
             var video = document.querySelector('video');
             var ctx = canvas.getContext('2d');
             canvas.width = parseInt(video.offsetWidth);
             canvas.height =  parseInt(video.offsetHeight);
             ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
             var a = document.createElement('a');
             a.download = 'snap-' + canvas.width + 'x' + canvas.height + '-' + video.currentTime + '.jpg';
             a.href = canvas.toDataURL('image/jpeg');
             document.body.appendChild(a).click();
             a.remove();
            })(window, document)
            """)
    driver.close()
screenShotVideoYT("uYhT8FL9aHo","60")