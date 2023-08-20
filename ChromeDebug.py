from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()


options.add_experimental_option("debuggerAddress","localhost:9222")


driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.netflix.com/bd/login")
driver.find_element(By.ID,'id_userLoginId').send_keys("fardinahosan@gmail.com")

