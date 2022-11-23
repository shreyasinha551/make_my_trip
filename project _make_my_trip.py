from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

import time

driver= webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
window= driver.get("https://www.makemytrip.com/")
login= driver.find_element(By.XPATH,"//li[@class='makeFlex hrtlCenter font10 makeRelative lhUser userLoggedOut']")
login.click()

email_id= driver.find_element(By.ID,"username")
email_id.send_keys("shreya@gmail.com")


driver.refresh()
time.sleep(3)

list= driver.find_element(By.XPATH,"//input[@id='fromCity']")
list.send_keys("DEL")
time.sleep(3)
driver.find_element(By.XPATH,"//p[text()='New Delhi, India']").click()
list.send_keys(Keys.RETURN)

list_to= driver.find_element(By.XPATH,"//input[@id='toCity']")
list_to.send_keys("PUNE")
time.sleep(3)
driver.find_element(By.XPATH,"//p[text()='Pune, India']").click()
list_to.send_keys(Keys.RETURN)
# driver.implicitly_wait(5)
# driver.find_element(By.XPATH,"//span[text()='DEPARTURE']").click()
# driver.find_element(By.XPATH,"//div[@aria-label='Thu Nov 03 2022']").click()
#
search = driver.find_element(By.XPATH,"//a[text()='Search']")
search.click()
time.sleep(3)
driver.find_element(By.XPATH,"//button[text()='OKAY, GOT IT!']").click()

time.sleep(3)

view_prices= driver.find_element(By.XPATH,"(//span[text()='View Prices'])[1]").click()
time.sleep(3)
book_now= driver.find_element(By.XPATH,"(//button[text()='Book Now'])[1]").click()
time.sleep(5)





