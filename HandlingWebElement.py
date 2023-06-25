from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))

driver.get("https://discord.com/login")
driver.maximize_window()

driver.find_element(By.ID,'uid_5').send_keys("fardinaero1@gmail.com")
driver.find_element(By.ID,'uid_7').send_keys("fardinaero1@gmail.com")
driver.find_element(By.XPATH,'//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/button[2]').click()
