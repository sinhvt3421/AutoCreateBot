from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def upimage(drv,img,id):
    i = 0
    while(i < 5):
        try:
            #avatar 
            drv.find_element_by_class_name("_156p").click()
            time.sleep(2)
            up = drv.find_element_by_xpath("//input[@title='Choose a file to upload']")
            up.send_keys(img + "1.jpg")
            time.sleep(5)
            save = drv.find_element_by_xpath("//button[@data-testid='profilePicSaveButton']")
            save.click()
            time.sleep(5)
            break
        except:
            i = i + 1
            continue
    i = 0
    while(i < 5):
        try:
            #banner
            drv.get("http://facebook.com/"+id)
            up2 = drv.find_element_by_class_name("fbTimelineEditCoverButton")
            up2.click()
            time.sleep(2)
            cover = drv.find_element_by_xpath("//input[@title='Choose a file to upload']")
            cover.send_keys(img + "2.jpg")
            time.sleep(1)
            save2 = drv.find_element_by_xpath("//button[@name='save']")
            save2.click()
            break
        except:
            i = i + 1
            continue
