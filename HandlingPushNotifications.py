import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://push-notifications-demo.netlify.app/")
driver.find_element(By.ID,'ask-user-permission-button').click()
