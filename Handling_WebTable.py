import time
from selenium import webdriver
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


driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.way2automation.com/angularjs-protractor/webtables/")


#-------------First Method-------------------------
row_count = driver.find_elements(By.XPATH,'//tbody/tr')
total_rows =len(row_count)
#
column_count = driver.find_elements(By.XPATH,'//tbody/tr[1]/td')
total_colums =len(column_count)
#
#
# for i in row_count:
#     print("Row : "+i.text)
#

#-------------Second Method-------------------------

start_path ="//tbody/tr["
mid_path ="]/td["
end_path ="]"

for row in range(1,total_rows+1):
    for col in range(1,total_colums+1):
        final_path = start_path+str(row)+mid_path+str(col)+end_path
        print(driver.find_element(By.XPATH,final_path).text,end=" ")
    print()
