from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.google.com')

print(driver.title)
print(driver.current_url)
print(driver.name)
print(driver.desired_capabilities)