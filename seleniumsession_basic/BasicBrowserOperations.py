from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
#driver = webdriver.Firefox(GeckoDriverManager().install())
driver.get("https://www.google.com")

driver.maximize_window()
print(driver.title)
print(driver.current_url)
print(driver.name)
print(driver.desired_capabilities)