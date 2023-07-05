import time
from selenium  import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
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
driver.get("https://www.way2automation.com/")

#Create Action object
Action=ActionChains(driver)

#find element with xapth and save it to a menu variable
menu=driver.find_element(By.XPATH,'//*[@id="menu-item-27597"]/a')
#perfom action to menu variable
Action.move_to_element(menu).perform()
#find and click for sub element
driver.find_element(By.XPATH,'//*[@id="menu-item-27602"]/a')


