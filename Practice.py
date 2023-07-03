import time
from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.youtube.com/")

main_element = driver.find_elements(By.TAG_NAME,'a')
for i in main_element:
    url_name=i.text
    url_url=i.get_attribute('href')
    if url_name is not None and url_url is not None:
        print("Url Name: "+url_name,"Url is :"+url_url )
    else:
        print("No Links Found`")



