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
driver.get("https://deluxe-menu.com/popup-mode-sample.html")

right_menu_click =driver.find_element(By.XPATH,'/html/body/div/table/tbody/tr/td[2]/div[2]/table[1]/tbody/tr/td[3]/p[2]/img')
ActionChains(driver).context_click(right_menu_click).perform()
driver.find_element(By.XPATH,'/html/body/div/table/tbody/tr/td[2]/div[2]/table[1]/tbody/tr/td[3]/div[5]/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[1]').click()
driver.find_element(By.XPATH,'//td[@id="dm2m2i1tdT"]').click()
driver.find_element(By.XPATH,'//td[@id="dm2m3i0tdT"]').click()

