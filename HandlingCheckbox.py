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

driver.get("http://www.tizag.com/htmlT/htmlcheckboxes.php")
first_narrow = driver.find_element(By.XPATH,'/html/body/table[3]/tbody/tr[1]/td[2]/table/tbody/tr/td/div[4]')
second_narrow =first_narrow.find_elements(By.NAME,'sports')
for i in second_narrow:
        i.click()
print(len(second_narrow))
