from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def upimage(drv):
    #avatar 
    drv.find_element_by_class_name("_156p").click()
    time.sleep(2)
    drv.find_element_by_xpath("//input[@title='Choose a file to upload']").send_keys("/home/son/Desktop/image/avatar/1.jpg")
    time.sleep(5)
    drv.find_element_by_xpath("//button[@data-testid='profilePicSaveButton']").click()
    time.sleep(5)
    #banner
    drv.get("http://facebook.com/"+id)
    drv.find_element_by_xpath("//i[@class='_30vz img sp_KCuzLm96iNl sx_123333']").click()
    time.sleep(1)
    drv.find_element_by_xpath("//input[@title='Choose a file to upload']").send_keys("/home/son/Desktop/image/banner/1.jpg")
    time.sleep(1)
    drv.find_element_by_xpath("//button[@name='save']").click()
