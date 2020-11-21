from tkinter.tix import Select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\\Selenium\\browser\\chromedriver.exe")

driver.implicitly_wait(5)
driver.get("http://www.google.com")
print(driver.title)
driver.find_element_by_name("q").send_keys("hi vaibhav")
driver.maximize_window()

select  = Select(driver.find_element(By.ID, "name"))
select.select_by_index()
