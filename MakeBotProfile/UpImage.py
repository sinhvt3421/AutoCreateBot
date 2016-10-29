from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def upimage(drv,img,id):
    while(True):
        try:
            #avatar 
            drv.find_element_by_class_name("_156p").click()
            time.sleep(2)
            drv.find_element_by_xpath("//input[@title='Choose a file to upload']").send_keys("/home/sinh/Desktop/Bot/img" + "1.jpg")
            time.sleep(5)
            drv.find_element_by_xpath("//button[@data-testid='profilePicSaveButton']").click()
            time.sleep(5)
        except:
            continue
    while(True):
        try:
            #banner
            drv.get("http://facebook.com/"+id)
            drv.find_element_by_class_name("fbTimelineEditCoverButton").click()
            time.sleep(2)
            drv.find_element_by_xpath("//input[@title='Choose a file to upload']").send_keys("/home/sinh/Desktop/Bot/img" + "2.jpg")
            time.sleep(1)
            drv.find_element_by_xpath("//button[@name='save']").click()
        except:
            continue
