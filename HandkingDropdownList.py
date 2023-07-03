import time
from selenium  import webdriver
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
driver.get("https://www.wikipedia.org/")

#-----------------Drop Down Selection Start--------------------------------

# dropdownlist: WebElement=driver.find_element(By.ID,'searchLanguage')
#Select(dropdownlist).select_by_visible_text("English") --Using Solid Text
# Select(dropdownlist).select_by_value('af') -- Usig Value inside option tag

#------------------------Find & Print all List components--------------------------------------------

# lists=driver.find_elements(By.TAG_NAME,'option')
# for i in lists:
#     print("Text is : "+ i.text)

#-----------------Course Challenge--------------------------------
#-----------------Print All Title with URL in a page --------------------------------

# list_2 = driver.find_elements(By.TAG_NAME,'a')
# for links in list_2:
#      print("Link is : "+links.text,"URL: "+links.get_attribute("href"))
# print(len(list_2))

#-----------------Done--------------------------------

#-----------------------Find Spacific element inside a section-----------------------
# section_custom = driver.find_element(By.XPATH,"//*[@id=\"www-wikipedia-org\"]/div[7]")
# linkp =section_custom.find_elements(By.TAG_NAME,'a')
#
# for links in linkp:
#      print("Link is : " + links.text, "URL: " + links.get_attribute("href"))
# print(len(linkp))

#-----------------Course Challenge--------------------------------
#-----------------Click Link of same name id --------------------------------

# x_1= driver.find_element(By.XPATH,'//*[@id="www-wikipedia-org"]/div[2]')
# x_2=driver.find_elements(By.TAG_NAME,'a').__getitem__(220)
# print(x_2.get_attribute("href"))
# x_2.click()


