from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome('/usr/local/bin/chromedriver')

driver.get("https://rink.wintervillage.org/eventperformances.asp?evt=34")
#driver.implicitly_wait(20)
#try:
i = 1
while (len(driver.find_elements(By.ID, "loadMorePerformancesButton")) > 0 and i < 300):
    #driver.implicitly_wait(2)
    if (len(driver.find_elements(By.ID, "loadMorePerformancesButton")) < 1):
        print("no more button")
        break
    print("num of load more iterations")
    print(i)
    print("is there another button?")
    print(len(driver.find_elements(By.ID, "loadMorePerformancesButton")))
    i += 1    
    #wait = WebDriverWait(driver, 10)
    #element = wait.until(EC.element_to_be_clickable((By.ID, 'loadMorePerformancesButton')))
    try:
        button = driver.find_element(By.ID, "loadMorePerformancesButton")
        button.click()
    except:
        print("failed in loop")
        break
#finally:
#    print("failed in loop")
print("num of load more iterations")
print(i)
print("is there another button?")
print(len(driver.find_elements(By.ID, "loadMorePerformancesButton")))

#driver.implicitly_wait(10)

availibilty_status = driver.find_elements_by_class_name("pl-sale-status")
print(len(availibilty_status))
#availibilty_status = driver.find_elements(By.CLASS_NAME, "pl-sale-status")
#print(len(availibilty_status))



for i in availibilty_status:
    #if i.get_attribute('textContent') != 'Sold Out':
        print(i.get_attribute('textContent'))


elem = driver.find_element_by_xpath("//*")
source_code = elem.get_attribute("outerHTML")
#print(source_code)

print("beautiful soup")
html_doc = source_code
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
print(soup.find_all("div", {"class": "pl-sale-status"}))

#driver.close()