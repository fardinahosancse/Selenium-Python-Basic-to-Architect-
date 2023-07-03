import time
from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))


driver.maximize_window()
driver.implicitly_wait(20)


driver.get("https://www.netflix.com/bd/login")
print(driver.title)

wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.ID, 'id_password')))


driver.find_element(By.ID,'id_userLoginId').send_keys("fardinaero1@gmail.com")
driver.find_element(By.ID,'id_password').send_keys("fardinaero1@gmail.com")
driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button').click()
print(driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/div/div[2]').text)



