from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def setting(drv):
    drv.get("https://www.facebook.com/settings?tab=language&section=account&view")
    time.sleep(1)
    language = drv.find_element_by_xpath("//select[@name='new_language']")
    language.click()
    english = language.find_element_by_xpath("option[@value='en_GB']")
    english.click()
    print("ok")
    save = drv.find_element_by_id("u_0_7")
    save.click()
