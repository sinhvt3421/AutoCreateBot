from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

def sendRequest(drv):
    id = ["560381171","100004403798308","100002829114290"]
    for i in id:
        drv.get("www.facebook.com/" + i)
        time.sleep(2)
        try:
            add = drv.find_element_by_class_name("addButton")
            add.click()
            time.sleep(2)
        except:
            print(Exception.args)
        action = ActionChains(drv)
        action.send_keys(Keys.ENTER)
        img = drv.find_element_by_class_name("coverImage")
        img.click()
        time.sleep(3)
        action.send_keys('l')
        action.perform()
        time.sleep(2)
        action.send_keys(Keys.ESCAPE)
        action.perform()
        time.sleep(1)

def likeFanpage(drv):
    id = ["253442931350130","552298268194881","484451281604769"]
    for i in id:
        drv.get("www.facebook.com/" + i)
        time.sleep(2)
        like = drv.find_element_by_xpath("//div/button[@data-testid='page_timeline_like_button_test_id']")
        time.sleep(1)
        like.click()
        page = drv.find_element_by_class_name("_qk8")
        action = ActionChains(drv)
        action.move_by_offset(100,100)
        action.perform()
        time.sleep(1)
        action.send_keys(Keys.PAGE_DOWN)
        action.perform()
        time.sleep(2)
        action.send_keys(Keys.PAGE_DOWN)
        action.perform()
        time.sleep(3)