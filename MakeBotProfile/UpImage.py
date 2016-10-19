from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
#login
driver.get("http://facebook.com")
driver.find_element_by_id('email').send_keys("hoangminh.le12302@gmail.com")
driver.find_element_by_id('pass').send_keys("hoangminh12302")
time.sleep(1)
driver.find_element_by_id("u_0_l").submit()
time.sleep(1)
id = "100011474121516"
driver.get("http://facebook.com/"+id)
#avatar 
driver.find_element_by_class_name("_156p").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@title='Choose a file to upload']").send_keys("/home/son/Desktop/image/avatar/1.jpg")
time.sleep(5)
driver.find_element_by_xpath("//button[@data-testid='profilePicSaveButton']").click()
time.sleep(5)
#banner
driver.get("http://facebook.com/"+id)
driver.find_element_by_xpath("//i[@class='_30vz img sp_KCuzLm96iNl sx_123333']").click()
time.sleep(1)
driver.find_element_by_xpath("//input[@title='Choose a file to upload']").send_keys("/home/son/Desktop/image/banner/1.jpg")
time.sleep(1)
driver.find_element_by_xpath("//button[@name='save']").click()
