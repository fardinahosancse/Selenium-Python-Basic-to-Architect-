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
options.add_argument("--headless")

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://fardinahosan.netlify.app/")

# Take a full-page screenshot
s = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
width = s('Width') or 1920  # Set a default width if s('Width') returns None
height = s('height') or 1080  # Set a default height if s('height') returns None
driver.set_window_size(int(width), int(height))
driver.find_element(By.TAG_NAME, 'body').screenshot('./ss/fullpage.jpg')

# Close the driver
driver.quit()
