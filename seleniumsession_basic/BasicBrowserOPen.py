from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com")
driver.maximize_window()
assert "Google1" in driver.title

driver.find_element_by_name('q').send_keys("hi")
