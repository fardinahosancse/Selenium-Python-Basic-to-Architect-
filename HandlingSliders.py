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
driver.get("https://jqueryui.com/resources/demos/slider/default.html")

mainSlider = driver.find_element(By.ID,"slider")
size = mainSlider.size
location =mainSlider.location

print(location)
print(size)



Actions=ActionChains(driver)
slider=driver.find_element(By.XPATH,'//*[@id="slider"]')
Actions.drag_and_drop_by_offset(slider,size['width']/2,0).perform()