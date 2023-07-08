import time
from selenium  import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.alert import Alert
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


driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/div[2]/form/div[1]/div[2]/div[2]/div[2]/div/input[2]').click()
alert = Alert(driver)
print(alert.text)
time.sleep(3)
alert.accept()
