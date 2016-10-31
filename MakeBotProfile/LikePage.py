import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

def do_like(drv,id):
    while(True):
        try:
            npage = 2
            #go to profile
            btn = drv.find_element_by_xpath("//a[@data-testid='blue_bar_profile_link']")
            btn.click()
            drv.get("wwww.facebook.com/" + id + "/likes")
            # get likes tab 
            html_list = drv.find_element_by_xpath("//div[@role='tablist']")
            tab_list = html_list.find_elements_by_xpath("//a[@role='tab']")
            drv.execute_script("window.scrollTo(0, 200)")
            for i in range(0, 5):
                tab_list[i].click()
                time.sleep(2)
                for j in range(0, npage):
                    btn = drv.find_element_by_class_name("_vfm")
                    btn.click()
                    time.sleep(5)
                time.sleep(2)
            break
        except:
            continue
    