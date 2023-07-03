import time
from selenium  import webdriver
from selenium.common import NoSuchElementException
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

driver.get("https://www.netflix.com/bd/login")

#syntax of XPATH
#  //input[@id='identifierId']
"""
<input type="password" 
data-uia="password-field" 
name="password" 
class="nfTextField error" 
id="id_password" 
value="" 
tabindex="0" 
autocomplete="password" 
spellcheck="false" 
dir="" 
placeholder="">
"""



driver.find_element(By.XPATH,'//input[@id="id_password"]').send_keys("Fardinahosan")