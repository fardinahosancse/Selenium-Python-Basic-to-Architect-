import time
from selenium  import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
perfs={"profile.default_content_setting_values.notification":2}
options.add_experimental_option("detach", True)
options.add_experimental_option("perfs", perfs)
driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)


driver.get("https://web.dev/push-notifications-display-a-notification/")