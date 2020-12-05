from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


browserName = input("Enter browser name on which you want to execute script ")
if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == 'ff':
    driver = webdriver.Firefox(executable_path= GeckoDriverManager().install())
elif browserName == 'edge':
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
else:
    print("Enter correct browser name")

driver.get("https://www.google.com")
driver.get("https://www.facebook.com")
driver.back()
driver.forward()
