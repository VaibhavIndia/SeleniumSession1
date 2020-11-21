from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com")
print(driver.title)
driver.get("https://www.facebook.com")
print(driver.title)
driver.back()
print(driver.title)
driver.forward()
print(driver.title)
driver.quit()
