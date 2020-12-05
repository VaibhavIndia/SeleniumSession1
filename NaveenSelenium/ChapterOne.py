from selenium import  webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
#driver = webdriver.Chrome(executable_path= "C:\\Selenium\\drivers\\chromedriver.exe")
driver.get("https://www.google.com")
driver.maximize_window()
driver.find_element_by_name("q").send_keys("Naveen Automationlabs")
allElements = driver.find_elements(By.CSS_SELECTOR, "ul.erkvQe li span")
print(len(allElements))

for word in allElements:
    print(word.text)
    if word.text == "naveen automationlabs youtube":
        word.click()
        break
print(driver.title)
