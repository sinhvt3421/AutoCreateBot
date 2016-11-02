from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

def setting(drv):
    try:
        action = ActionChains(drv)
        drv.get("https://www.facebook.com/settings?tab=language&section=account&view")
        time.sleep(1)
        language = drv.find_element_by_xpath("//select[@name='new_language']")
        language.click()
        time.sleep(2)
        english = language.find_element_by_xpath("option[@value='en_GB']")
        action.click(english)
        action.perform()
        time.sleep(2)
        save = drv.find_element_by_id("u_0_7")
        save.submit()
        time.sleep(4)
    except:
        pass
