from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

#browsername = input("Enter browserName")
browsername = "firefox"
if browsername == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browsername == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
else:
    print("invlaid browser")

driver.get("https://www.google.com")

inputbox = driver.find_element(By.NAME,'q')
print(inputbox.is_displayed())
print(inputbox.is_enabled())

driver.get("https://www.geeksforgeeks.org/html-button-disabled-attribute/")
disable_btn = driver.find_element(By.XPATH,"//img[@title='Click to enlarge']")
print(disable_btn.is_enabled())
print(disable_btn.is_displayed())