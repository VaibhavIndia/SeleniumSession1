from selenium import  webdriver
from webdriver_manager.chrome import ChromeDriverManager

#driver=webdriver.Chrome(executable_path="")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com")