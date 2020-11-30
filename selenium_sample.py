from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('/usr/local/bin/chromedriver')

driver.get("https://mystuff.bublup.com/mybublup/#/mystuff/top/folder")
print(driver.title)
driver.implicitly_wait(6)
email_bar = driver.find_element_by_id("email")
email_bar.clear()
email_bar.send_keys("vihagupta95@gmail.com")
pass_bar = driver.find_element_by_id("password")
pass_bar.clear()
pass_bar.send_keys("HW191Dbub!")
button = driver.find_element_by_id("sign-in-submit")
button.click()

#driver.close()