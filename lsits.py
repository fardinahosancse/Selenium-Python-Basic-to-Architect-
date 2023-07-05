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

driver.get("https://www.udemy.com/course/selenium-python-tutorial/")
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div[1]/div[5]/div/div[4]/div/button').click()
ab=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div[1]/div[5]/div/div[4]/div')
dc=ab.find_elements(By.CLASS_NAME,'section--section-title--wcp90')
p=0
for i in dc:
    p+=1
    print(p,'-',i.text)
