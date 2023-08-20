import time
from selenium  import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress","localhost:9222")
driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager(version='114.0.5735.90').install()))
driver.maximize_window()
driver.implicitly_wait(10)



##------------Find LInk using its property and click--------------------##
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# div = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[2]/div[1]')
# links = div.find_elements(By.TAG_NAME,'a')
#
# for link in links:
#     href = link.get_attribute('href')
#     if "Laura" in href:
#         print(f"Found link with 'Laura' in href: {href}")
#         link.click()
#         break


##------------Check wheather a component is present or displayed or visibled in the page or not--------------------##
# driver.get("https://www.netflix.com/bd/login")
# def is_displayed(how,what):
#     try:
#         driver.find_element(by=how,value=what)
#         return True
#     except NoSuchElementException:
#         return False
#
# print(is_displayed(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div/div/label/input"))

# #--------------Mouseover ELements------------------------------------------
# driver.get("https://www.daraz.com.bd/")
# action = ActionChains(driver)
# menu = driver.find_element(By.XPATH,'//*[@id="Level_1_Category_No6"]/a/span')
# sub_menu = menu.find_element(By.XPATH,'//*[@id="J_3442298940"]/div/ul/ul[6]/li[1]/a/span')
# action.move_to_element(menu).perform()
# action.move_to_element(sub_menu).perform()
# macro_menu = sub_menu.find_element(By.XPATH,'//*[@id="J_3442298940"]/div/ul/ul[6]/li[1]/ul/li[1]/a/span').click()

#---------Handliing Slider--------------------------------
# driver.get("https://jqueryui.com/resources/demos/slider/default.html")
# main_slider = driver.find_element(By.XPATH,'//*[@id="slider"]')
# location = main_slider.location
# size = main_slider.size
# w,h = size['width'],size['height']
# print(location,size)
# print(w,h)
# ActionChains(driver).drag_and_drop_by_offset(main_slider,950,0).perform()


# #---------Handling Resizable--------------------------------
# driver.get("https://jqueryui.com/resources/demos/resizable/default.html")
# content =  driver.find_element(By.XPATH,'//*[@id="resizable"]/div[3]')
# ActionChains(driver).drag_and_drop_by_offset(content,100,100).perform()

##---------------Handling RightClick--------------------

# driver.get("https://deluxe-menu.com/popup-mode-sample.html")
#
# driver.get("https://deluxe-menu.com/popup-mode-sample.html")
#
# right_menu_click =driver.find_element(By.XPATH,'/html/body/div/table/tbody/tr/td[2]/div[2]/table[1]/tbody/tr/td[3]/p[2]/img')
# ActionChains(driver).context_click(right_menu_click).perform()
# driver.find_element(By.XPATH,'/html/body/div/table/tbody/tr/td[2]/div[2]/table[1]/tbody/tr/td[3]/div[5]/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[1]').click()
# driver.find_element(By.XPATH,'//*[@id="dm2m2i1tdT"]').click()
# driver.find_element(By.XPATH,'//td[@id="dm2m3i0tdT"]').click()


#--------------------Switch To---------------------------------------


#----------------------Handling Alerts----------------------------------

driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/div[2]/form/div[1]/div[2]/div[2]/div[2]/div/input[2]').click()
Alert(driver).accept()


#-------------------Handling IFRAME USING SWITCH TO-----------------------------------
# driver.get('https://fardinadad.w3spaces.com/')
# driver.switch_to.frame('iframeResult')
# driver.find_element(By.XPATH,'/html/body/button[1]').click()


# #-------------------Handling Popup------------------
# driver.get('https://www.lambdatest.com/')
# driver.switch_to.window(driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div[2]/div/span[1]').click())

import re


def check_password_validity(password):
    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False

    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False

    # Check for at least one digit
    if not re.search(r'\d', password):
        return False

    # Check for at least two special characters
    if len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', password)) < 2:
        return False

    # Check for minimum and maximum length
    if len(password) < 10 or len(password) > 24:
        return False

    return True


# Get user input for the password
user_password = input("Enter a password: ")

# Check password validity
is_valid = check_password_validity(user_password)

if is_valid:
    print("Password is valid.")
else:
    print("Password is not valid.")
