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





driver.find_element(By.XPATH,"//input[@id='id_userLoginId']").send_keys("cfesrfvrdrvbrfbv")
driver.find_element(By.XPATH,"//input[@id='id_password']").send_keys("cfesrfvrdrvbrfbv")
driver.find_element(By.XPATH,"//button[normalize-space()='Sign In']").click()

