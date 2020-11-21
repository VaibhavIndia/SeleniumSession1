from selenium import  webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.utils import ChromeType

browserName = "firefox"

if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path = GeckoDriverManager().install())
elif browserName == "chromium":
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
else:
    print("error in browsername")

driver.maximize_window()
driver.get("https://www.google.com")
driver.find_element(By.ID,"q").send_keys("hi")