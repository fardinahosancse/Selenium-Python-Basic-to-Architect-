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

#------------Method 1-----------

# def is_elemement_present(xpath):
#     try:
#         driver.find_element(By.ID,id)
#         return True
#     except NoSuchElementException:
#         return False


from selenium.common.exceptions import NoSuchElementException
#------------Method 2-----------
# def is_element_present(how,what):
#     try:
#         driver.find_element(by=how, value=what)
#         return True
#     except NoSuchElementException:
#         return False
#
# print(is_element_present(By.XPATH,'//*[@id="id_password"]'))

#------------Method 3-----------

def is_elemnt_present(how,what):
    if len(driver.find_elements(by=how,value=what)) is not 0:
        return False
    else:
        return True

print(is_elemnt_present(By.XPATH,'//*[@id="id_password"]'))